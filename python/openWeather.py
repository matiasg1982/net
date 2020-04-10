import json
import sqlite3
import requests
from datetime import datetime

import sys

#user openWeather  user = matiasg1982 pass: openweather1982

class OpenWeather:

    appId = "4db57c8b7fdf999821102b46ffc8ffac"
    
    def __init__(self):
        #create table
        self.conn = sqlite3.connect("open_weather.db")
        self.cur = self.conn.cursor()
        self.units = "metric"
        self.countries = []

    def CreateDB(self):
        self.cur.execute("CREATE TABLE IF NOT EXISTS cities (id INTEGER, name TEXT, country TEXT, lon REAL, lat REAL);")
        self.cur.execute("CREATE TABLE IF NOT EXISTS countries (id INTEGER, name TEXT);")
        
        self.conn.commit()
      
    def InsertDataCitiesJson(self):
        with open("city.list.json") as city_file:
            data_cities=json.load(city_file)
        for enum,city in enumerate(data_cities):    
            self.cur.execute("INSERT INTO cities VALUES (?, ?, ?, ?, ?)",(city["id"],city["name"],city["country"],city["coord"]["lon"],city["coord"]["lat"]))
        self.conn.commit()

    def InsertDataCountriesJson(self):
        with open("country.list.json") as country_file:
            data_countries=json.load(country_file)
        for enum,country in enumerate(data_countries):    
            self.cur.execute("INSERT INTO countries VALUES (?, ?)",(country["Code"],country["Name"]))
        self.conn.commit()

    def GetIdByCity(self,city_name,country='',similar=False):
        if country == '':
            if similar :
                self.cur.execute("SELECT * FROM cities WHERE name like ? limit 1",('%'+city_name+'%',))
            else:    
                self.cur.execute("SELECT * FROM cities WHERE name = ? ",(city_name,))
        else:
            if similar :
                self.cur.execute("SELECT * FROM cities WHERE name like ? and country like ? limit 1",('%'+city_name+'%', '%'+country+'%'))
            else:    
                self.cur.execute("SELECT * FROM cities WHERE name = ? and country=?",(city_name,country))
        result = self.cur.fetchone()
        if (result != None and len(result)>0):
            self.city_name_found = result[1]
            self.country_name_found = result[2]
        else:
            self.city_name_found = ""

        return result[0] if (result != None and len(result)>0) else 0

    def GetIdByCountry(self,country):
        self.cur.execute("SELECT * FROM countries WHERE name = ? ",(country,))
        result = self.cur.fetchone()
        return result[0] if (result != None and len(result)>0) else ""

    def GetCountries(self):
        self.cur.execute("SELECT * FROM countries")
        result = self.cur.fetchall()
        countries = []
        for country in result:
            countries.append({"id" : country[0] , "country" : country[1]})
        self.countries = countries
        return countries

    def GetWeatherById(self,id_city):
        result = requests.get(f'http://api.openweathermap.org/data/2.5/forecast?id={id_city}&units={self.units}&APPID={self.appId}')
        return result.text

    def GetTemperatureByCity(self,city,country):
        id_country = self.GetIdByCountry(country)
        id_city = self.GetIdByCity(city,id_country)

        if id_city == 0:
            id_city = self.GetIdByCity(city,id_country,True)

        result = self.GetDataByApi(id_city)
        return result[0] if len(result)>0 else {"temp":"Not Found"}

    def GetDataByApi(self,id_city):
        
        result_weather = self.GetWeatherById(id_city)
        result_weather = json.loads(result_weather)
        
        result=[]
        if result_weather["cod"] != "400":
            if type(result_weather["list"]) == list : 
                for weather in result_weather["list"]:
                    dt = datetime.fromtimestamp(weather["dt"]).strftime('%Y-%m-%d %H')
                    temp = weather["main"]["temp"]
                    temp_min = weather["main"]["temp_min"]
                    temp_max = weather["main"]["temp_max"]
                    #print(f'Time:{dt} Temp:{temp} Temp Min:{temp_min} Temp Max:{temp_max}')
                    
                    row = { "datetime": dt , "temp": temp , "temp_max": temp_max , "temp_min": temp_min}
                    result.append(row)
        return result



default_city = "Valencia"
default_country = "Spain"

city=""
country=""
if len(sys.argv)>=2 :
    if len(sys.argv)==3:
        country = sys.argv[2]
        city = sys.argv[1]
    else:    
        city = sys.argv[1]
else:
    country = default_country
    city = default_city

weather = OpenWeather()
temp = weather.GetTemperatureByCity(city,country)

print(f'City {weather.city_name_found} - {weather.country_name_found}')
print(temp["temp"])