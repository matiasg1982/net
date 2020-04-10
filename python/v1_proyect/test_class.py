from openWeather import OpenWeather
import sys
 

city=""
country=""
if len(sys.argv)>=2 :
    if len(sys.argv)==3:
        country = sys.argv[2]
        city = sys.argv[1]
    else:    
        city = sys.argv[1]
else:
    country = "Valencia"
    city = "Spain"
 
w = OpenWeather()
temp = w.GetTemperatureByCity(city,country)

print(f'City {w.city_name_found} - {w.country_name_found}')
print(temp["temp"])