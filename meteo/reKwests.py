from datetime import datetime
import json
import requests

api_url = "https://api.open-meteo.com/v1/forecast?"

apen = "latitude=51.22&longitude=4.40&hourly=temperature_2m"
snt_mnca = "latitude=34.02&longitude=-118.49&hourly=temperature_2m"
tkyo = "latitude=35.69&longitude=139.69&hourly=temperature_2m"

# api = requests.get("https://open-meteo.com/en/docs#api_form")


# city = input("give me a city ")

# response = requests.post(url, data={'select_city': api})

# print("antwerpen" in response.text)
    
url = requests.get(api_url + apen)

weather_info = url.json()

time = weather_info['hourly']['time']
temp = weather_info['hourly']['temperature_2m']

time_temp = dict(zip(time, temp))

print(time_temp)
