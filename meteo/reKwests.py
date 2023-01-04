from datetime import datetime
import json
import requests

api_url = "https://api.open-meteo.com/v1/forecast?" 

apen = "latitude=51.22&longitude=4.40&hourly=temperature_2m"
snt_mnca = "latitude=34.02&longitude=-118.49&hourly=temperature_2m"
tkyo = "latitude=35.69&longitude=139.69&hourly=temperature_2m"

selection = input("Which city's temperature should I plot on a graph? \n Antwerp? Santa Monica? Tokyo?\n")

# if selection == "Antwerp":
#     def which_city():
#         requests.get(api_url + apen)
#         return
# elif selection == "Santa Monica":
#     def which_city():
#         requests.get(api_)
# c1 = which_city()

# print(c1)

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

which_city(selection)

def weath_info():
    url = which_city(selection)
    print(url.json())

weath_info()



# city = input("give me a city ")

# response = requests.post(url, data={'select_city': api})

    
# url = requests.get(api_url + apen)

# weather_info = url.json()

# time = weather_info['hourly']['time']
# temp = weather_info['hourly']['temperature_2m']

# time_temp = dict(zip(time, temp))

# print(time_temp)