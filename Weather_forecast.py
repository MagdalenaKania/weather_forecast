import urllib.request
import json



cities = ["Wroclaw,pl", "Warsaw,pl", "Krakow,pl", "London,uk", "New+York,us", "Los+Angeles,us", "Barcelona,es", "Dubai,uae", "Tokio,jpn", "Melbourne,aus" ]
my_url_template = "https://openweathermap.org/data/2.5/weather?q=%s&appid=b6907d289e10d714a6e88b30761fae22"

info = []

for i in cities:
    response = urllib.request.urlopen(my_url_template % i)
    info2 = json.loads(response.read())
    info.append(info2)

info_Wroclaw = info[0]
info_Warsaw = info[1]
info_Cracow = info[2]
info_London = info[3]
info_NewYork = info[4]
info_LosAngeles = info[5]
info_Barcelona = info[6]
info_Dubai = info[7]
info_Tokio = info[8]
info_Melbourne = info[9]


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
            self.temp) + " Celsius degrees, the minimum temperature is " + str(self.temp_min) + ", and the maximum " + str(
            self.temp_max) + " Celsius degrees. The pressure is " + str(
            self.pressure) + " hPa and relative humidity is " + str(self.humidity) + " %."


my_city = []

Wrocław = Weather(info_Wroclaw)
my_city.append(Wrocław)

Warszawa = Weather(info_Warsaw)
my_city.append(Warszawa)

Kraków = Weather(info_Cracow)
my_city.append(Kraków)

Londyn = Weather(info_London)
my_city.append(Londyn)

Nowy_Jork = Weather(info_NewYork)
my_city.append(Nowy_Jork)

Los_Angeles = Weather(info_LosAngeles)
my_city.append(Los_Angeles)

Barcelona = Weather(info_Barcelona)
my_city.append(Barcelona)

Dubaj = Weather(info_Dubai)
my_city.append(Dubaj)

Tokio = Weather(info_Tokio)
my_city.append(Tokio)

Melbourne = Weather(info_Melbourne)
my_city.append(Melbourne)


print(
    "Hello! Welcome to the 'Weather forecast' program.\nChoose a city from the list and get to know the weather:  \n1. Wroclaw\n2. Warsaw\n3. Krakow\n4. London\n5. New York\n6. Los Angeles\n7. Barcelona\n8. Dubai\n9. Tokio\n10. Melbourne ")
x = str(input("Select city:"))


def find_city():
    for i in my_city:
        if (i.name == x):
            return i
    return None


found_city = find_city()

if found_city==None:
    print("Wrong city, please try again!")
else:
    print(found_city)

