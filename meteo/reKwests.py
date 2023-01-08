from datetime import datetime
from json import load, loads
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


weath_info = weath_info()

temp = weath_info['hourly']['temperature_2m']
print(temp)


def latitude():
    lat = format(weath_info['latitude'],".2f") 
    if float(lat) > 0:
        vert_direction = '°N'
    else:
        vert_direction = '°S'
    lat_direction = lat, vert_direction, ', '
    latitude_text = list(lat_direction)
    a_latitude = ''.join(latitude_text)
    return a_latitude

def longitude():
    long = format(weath_info['longitude'],".2f")
    if float(long) > 0:
        hor_direction = '°E'
    else:
        hor_direction = '°W'
    long_direction = long, hor_direction, ', '
    longitude_text = list(long_direction)
    a_longitude = ''.join(longitude_text)
    return a_longitude

def elevation():
    elevation = str(weath_info['elevation']), 'm ', 'above sea level'
    elevation_text = list(elevation)
    a_elevation = ''.join(elevation_text)
    return a_elevation

def gen_time():
    gen_time = 'Generated in ', format(weath_info['generationtime_ms'],".2f"), 'ms,'
    gen_time_text = list(gen_time)
    a_gen_time = ''.join(gen_time_text)
    return a_gen_time

def timezone():
    timezone = 'time in ', weath_info['timezone'], '+0'
    timezone_text = list(timezone)
    a_timezone = ''.join(timezone_text)
    return a_timezone 

# now = datetime.now()
# print(now)

