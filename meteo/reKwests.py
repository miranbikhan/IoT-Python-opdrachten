from datetime import datetime
import requests
from json import load, loads

apen = requests.get("https://api.open-meteo.com/v1/forecast?latitude=51.22&longitude=4.40&hourly=temperature_2m")
snt_mnca = requests.get("https://api.open-meteo.com/v1/forecast?latitude=34.02&longitude=-118.49&hourly=temperature_2m")
tkyo = requests.get("https://api.open-meteo.com/v1/forecast?latitude=35.69&longitude=139.69&hourly=temperature_2m")
sao_paul = requests.get("https://api.open-meteo.com/v1/forecast?latitude=-23.55&longitude=-46.64&hourly=temperature_2m")

apen_info = apen.json()
snt_mnca_info = snt_mnca.json()
tkyo_info = tkyo.json()
sao_paul_info = sao_paul.json()

selection = ""

selection = input("Choose a city: \n 1. Antwerp \n 2. Santa Monica\n 3. Tokyo\n 4. Sao Paulo\n")


if selection == "Antwerp":
    def temp():
        temp = apen_info['hourly']['temperature_2m']
        return temp

    def latitude():
        lat = format(apen_info['latitude'],".2f") 
        if float(lat) > 0:
            vert_direction = '°N'
        else:
            vert_direction = '°S'
        lat_direction = lat, vert_direction,
        latitude_text = list(lat_direction)
        a_latitude = ''.join(latitude_text)
        return a_latitude

    def longitude():
        long = format(apen_info['longitude'],".2f")
        if float(long) > 0:
            hor_direction = '°E'
        else:
            hor_direction = '°W'
        long_direction = long, hor_direction
        longitude_text = list(long_direction)
        a_longitude = ''.join(longitude_text)
        return a_longitude

    def elevation():
        elevation = str(apen_info['elevation']), 'm ', 'above sea level'
        elevation_text = list(elevation)
        a_elevation = ''.join(elevation_text)
        return a_elevation

    def gen_time():
        gen_time = 'Generated in ', format(apen_info['generationtime_ms'],".2f"), 'ms,'
        gen_time_text = list(gen_time)
        a_gen_time = ''.join(gen_time_text)
        return a_gen_time

    def timezone():
        timezone = 'time in ', apen_info['timezone'], '+0'
        timezone_text = list(timezone)
        a_timezone = ''.join(timezone_text)
        return a_timezone 

    def text_top():
        text_top = (latitude(), longitude(), '', elevation())
        return text_top

    def text_bottom():
        text_bottom = (gen_time(), timezone())
        return text_bottom

elif selection == "Santa Monica":
    def temp():
        temp = snt_mnca_info['hourly']['temperature_2m']
        return temp

    def latitude():
        lat = format(snt_mnca_info['latitude'],".2f") 
        if float(lat) > 0:
            vert_direction = '°N'
        else:
            vert_direction = '°S'
        lat_direction = lat, vert_direction,
        latitude_text = list(lat_direction)
        a_latitude = ''.join(latitude_text)
        return a_latitude

    def longitude():
        long = format(snt_mnca_info['longitude'],".2f")
        if float(long) > 0:
            hor_direction = '°E'
        else:
            hor_direction = '°W'
        long_direction = long, hor_direction
        longitude_text = list(long_direction)
        a_longitude = ''.join(longitude_text)
        return a_longitude

    def elevation():
        elevation = str(snt_mnca_info['elevation']), 'm ', 'above sea level'
        elevation_text = list(elevation)
        a_elevation = ''.join(elevation_text)
        return a_elevation

    def gen_time():
        gen_time = 'Generated in ', format(snt_mnca_info['generationtime_ms'],".2f"), 'ms,'
        gen_time_text = list(gen_time)
        a_gen_time = ''.join(gen_time_text)
        return a_gen_time

    def timezone():
        timezone = 'time in ', snt_mnca_info['timezone'], '+0'
        timezone_text = list(timezone)
        a_timezone = ''.join(timezone_text)
        return a_timezone 

    def text_top():
        text_top = (latitude(), longitude(), '', elevation())
        return text_top

    def text_bottom():
        text_bottom = (gen_time(), timezone())
        return text_bottom

elif selection == "Tokyo":
    def temp():
        temp = tkyo_info['hourly']['temperature_2m']
        return temp

    def latitude():
        lat = format(tkyo_info['latitude'],".2f") 
        if float(lat) > 0:
            vert_direction = '°N'
        else:
            vert_direction = '°S'
        lat_direction = lat, vert_direction,
        latitude_text = list(lat_direction)
        a_latitude = ''.join(latitude_text)
        return a_latitude

    def longitude():
        long = format(tkyo_info['longitude'],".2f")
        if float(long) > 0:
            hor_direction = '°E'
        else:
            hor_direction = '°W'
        long_direction = long, hor_direction
        longitude_text = list(long_direction)
        a_longitude = ''.join(longitude_text)
        return a_longitude

    def elevation():
        elevation = str(tkyo_info['elevation']), 'm ', 'above sea level'
        elevation_text = list(elevation)
        a_elevation = ''.join(elevation_text)
        return a_elevation

    def gen_time():
        gen_time = 'Generated in ', format(tkyo_info['generationtime_ms'],".2f"), 'ms,'
        gen_time_text = list(gen_time)
        a_gen_time = ''.join(gen_time_text)
        return a_gen_time

    def timezone():
        timezone = 'time in ', tkyo_info['timezone'], '+0'
        timezone_text = list(timezone)
        a_timezone = ''.join(timezone_text)
        return a_timezone 

    def text_top():
        text_top = (latitude(), longitude(), '', elevation())
        return text_top

    def text_bottom():
        text_bottom = (gen_time(), timezone())
        return text_bottom

elif selection == "Sao Paulo":
    def temp():
        temp = sao_paul_info['hourly']['temperature_2m']
        return temp

    def latitude():
        lat = format(sao_paul_info['latitude'],".2f") 
        if float(lat) > 0:
            vert_direction = '°N'
        else:
            vert_direction = '°S'
        lat_direction = lat, vert_direction,
        latitude_text = list(lat_direction)
        a_latitude = ''.join(latitude_text)
        return a_latitude

    def longitude():
        long = format(sao_paul_info['longitude'],".2f")
        if float(long) > 0:
            hor_direction = '°E'
        else:
            hor_direction = '°W'
        long_direction = long, hor_direction
        longitude_text = list(long_direction)
        a_longitude = ''.join(longitude_text)
        return a_longitude

    def elevation():
        elevation = str(sao_paul_info['elevation']), 'm ', 'above sea level'
        elevation_text = list(elevation)
        a_elevation = ''.join(elevation_text)
        return a_elevation

    def gen_time():
        gen_time = 'Generated in ', format(sao_paul_info['generationtime_ms'],".2f"), 'ms,'
        gen_time_text = list(gen_time)
        a_gen_time = ''.join(gen_time_text)
        return a_gen_time

    def timezone():
        timezone = 'time in ', sao_paul_info['timezone'], '+0'
        timezone_text = list(timezone)
        a_timezone = ''.join(timezone_text)
        return a_timezone 

    def text_top():
        text_top = (latitude(), longitude(), '', elevation())
        return text_top

    def text_bottom():
        text_bottom = (gen_time(), timezone())
        return text_bottom




# print(weath_info['hourly']['temperature_2m'])

        

# def weath_info():
#     url = which_city()
#     weather_info = url.json()
#     return weather_info

# print(weath_info())


# def time():
#     t_t = weath_info()
#     time = t_t['hourly']['time']
#     return time


# weath_info = weath_info()

# temp = weath_info['hourly']['temperature_2m']

# print(temp)


# def latitude():
#     lat = format(weath_info['latitude'],".2f") 
#     if float(lat) > 0:
#         vert_direction = '°N'
#     else:
#         vert_direction = '°S'
#     lat_direction = lat, vert_direction,
#     latitude_text = list(lat_direction)
#     a_latitude = ''.join(latitude_text)
#     return a_latitude

# def longitude():
#     long = format(weath_info['longitude'],".2f")
#     if float(long) > 0:
#         hor_direction = '°E'
#     else:
#         hor_direction = '°W'
#     long_direction = long, hor_direction
#     longitude_text = list(long_direction)
#     a_longitude = ''.join(longitude_text)
#     return a_longitude

# def elevation():
#     elevation = str(weath_info['elevation']), 'm ', 'above sea level'
#     elevation_text = list(elevation)
#     a_elevation = ''.join(elevation_text)
#     return a_elevation

# def gen_time():
#     gen_time = 'Generated in ', format(weath_info['generationtime_ms'],".2f"), 'ms,'
#     gen_time_text = list(gen_time)
#     a_gen_time = ''.join(gen_time_text)
#     return a_gen_time

# def timezone():
#     timezone = 'time in ', weath_info['timezone'], '+0'
#     timezone_text = list(timezone)
#     a_timezone = ''.join(timezone_text)
#     return a_timezone 

# def text_top():
#     text_top = (latitude(), longitude(), '', elevation())
#     return text_top

# print(text_top())
