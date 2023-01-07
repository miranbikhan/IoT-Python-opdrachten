from datetime import datetime
import json
import requests

api_url = "https://api.open-meteo.com/v1/forecast?" 

apen = "latitude=51.22&longitude=4.40&hourly=temperature_2m"
snt_mnca = "latitude=34.02&longitude=-118.49&hourly=temperature_2m"
tkyo = "latitude=35.69&longitude=139.69&hourly=temperature_2m"

selection = input("Which city's temperature should I plot on a graph? \n Antwerp? Santa Monica? Tokyo?\n")

def which_city(selection):
    if selection == "Antwerp":
        url = requests.get(api_url + apen)
        return url
    elif selection == "Santa Monica":
        url = requests.get(api_url + snt_mnca)
        return url
    elif selection == "Tokyo":
        url = requests.get(api_url + tkyo)
        return url


def weath_info():
    url = which_city(selection)
    weather_info = url.json()
    return weather_info

def time():
    t_t = weath_info()
    time = t_t['hourly']['time']
    return time



which_city(selection)
weath_info()
print(time())

# def time_temp():

now = datetime.now()
print(now)

    
# url = requests.get(api_url + apen)

# weather_info = url.json()

# time = weather_info['hourly']['time']
# temp = weather_info['hourly']['temperature_2m']

# time_temp = dict(zip(time, temp))

# print(time_temp)