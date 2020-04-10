import json
import sqlite3

#url = requests.urllib3.get_host()

with open("city.list.json") as city_file:
    data_cities=json.load(city_file)

print(len(data_cities))

 