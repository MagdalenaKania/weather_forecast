import urllib.request
import json


class Weather(object):

    def __init__(self, city_info):
        self.name = city_info["name"]
        self.temp = city_info["main"]["temp"]
        self.temp_min = city_info["main"]["temp_min"]
        self.temp_max = city_info["main"]["temp_max"]
        self.pressure = city_info["main"]["pressure"]
        self.humidity = city_info["main"]["humidity"]

    def __str__(self):
        return "You have chosen: " + self.name + ". The temperature is " + str(
            self.temp) + " Celsius degrees, the minimum temperature is " + str(
            self.temp_min) + ", and the maximum " + str(
            self.temp_max) + " Celsius degrees. The pressure is " + str(
            self.pressure) + " hPa and relative humidity is " + str(self.humidity) + "%."


class City(object):

    def __init__(self, name, country):
        self.name = name
        self.country = country

    def __str__(self):
        normalized_name = self.name.replace("+", " ")
        return normalized_name + "," + self.country


cities = [City("Wroclaw", "pl"), City("Warsaw", "pl"), City("Krakow", "pl"), City("London", "uk"),
          City("New York", "us"), City("Los Angeles", "us"), City("Barcelona", "es"), City("Dubai", "uae"),
          City("Tokio", "jpn"), City("Melbourne", "aus")]

my_url_template = "https://openweathermap.org/data/2.5/weather?q=%s&appid=b6907d289e10d714a6e88b30761fae22"

city_jsons = []

for city in cities:
    response = urllib.request.urlopen(my_url_template % city)
    json = json.loads(response.read())
    city_jsons.append(json)

city_weathers = []

for city_json in city_jsons:
    city_weathers.append(Weather(city_json))

print("Hello! Welcome to the 'Weather forecast' program.\nChoose a city from the list and get to know the weather:")

for element in cities:
    print(element.name)

user_city = str(input("Select city:"))


def find_city():
    for city_weather in city_weathers:
        if city_weather.name == user_city:
            return city_weather
    return None


found_city = find_city()

if found_city is None:
    print("Wrong city, please try again!")
else:
    print(found_city)
