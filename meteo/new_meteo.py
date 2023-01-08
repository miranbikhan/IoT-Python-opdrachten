import turtle
from turtle import *
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


#all the variables needed
weer = temp()
weer_px = [i for i in weer]

cold = round(min(weer)) 
hot = round(max(weer))
total = cold - hot
steps = abs(total)
block  = round(400/steps)

#turtle code starts here
t = turtle.Turtle()
s = turtle.Screen()
s.colormode(255)
width, height = 1250, 650
s.setup(width, height)
t.speed(0)
s.delay(0)
# t.hideturtle()


# y-as starts here

def y_value_generator():
    list_hot = hot + 1
    y_axis = [*range(cold, list_hot)]
    return y_axis

def temp_y_axis():
    y_axis = y_value_generator()
    t.penup()
    x_start = -s.window_width() / 2 + 13
    y_start = -s.window_height() / 2 + 50   
    for y in y_axis:
        t.goto(x_start, y_start)
        t.pendown()
        t.write(y, align='center', font=("Arial", 11, "normal"))
        y_start += block
        t.penup()

temp_y_axis()
    

def y_axis_lines():
    x_start = -s.window_width() / 2 + 35
    y_l = -275 + 5
    t.pencolor((226, 226, 226))
    for l in range(steps):
        t.goto(x_start, y_l)
        t.setheading(0)
        t.pendown()
        t.forward(970)
        t.penup()
        y_l += block

y_axis_lines()

# x-as starts here

def bottom_x_axis():
    t.pencolor(0,0,0)
    x_start = -s.window_width() / 2 + 35
    y_start = -s.window_height() / 2 + 35
    t.goto(x_start, y_start)
    t.setheading(0)
    t.pendown()
    t.forward(970)
    t.penup()

bottom_x_axis()

def x_days():
    x_start = -s.window_width() / 2 + 45
    y_start = -s.window_height() / 2 + 34
    for d in range(4):
            t.goto(x_start, y_start)
            t.setheading(-90)
            t.pendown()
            t.pensize(2)
            t.forward(8)
            t.penup()
            t.forward(12)
            t.setheading(0)
            t.write('day', True, align="center", font=("Arial", 11, 'normal'))
            x_start += 240

x_days()

def x_noon():
    x_start = -s.window_width() / 2 + 165
    y_start = -s.window_height() / 2 + 34
    for d in range(4):
            t.pensize(0)
            t.goto(x_start, y_start)
            t.setheading(-90)
            t.pendown()
            t.forward(8)
            t.penup()
            t.forward(12)
            t.setheading(0)
            t.write('12:00', True, align="center")
            x_start += 240
x_noon()

def x_2h():
    x_start = -s.window_width() / 2 + 65
    y_start = -s.window_height() / 2 + 34
    for h in range(48):
            t.pensize(0)
            t.goto(x_start, y_start)
            t.setheading(-90)
            t.pendown()
            t.forward(4)
            t.penup()
            x_start += 20

x_2h()

    
def draw_line():
    t.penup()
    draw_sx = -580
    draw_sy = -275
    print('draw_sy:', draw_sy)
    t.goto(draw_sx, draw_sy)
    counter = 0
    for w in (weer_px):
        if counter < 97:
            t.color('cyan')
            w_y = (abs(w) - abs(cold) ) * block 
            draw_sy += abs(w_y)
            t.goto(draw_sx, draw_sy)
            t.pensize()
            t.pendown()
            t.pensize(2)
            t.color('cyan')
            t.dot()
            draw_sx += 10
            w_y = 0
            draw_sy = -275
            counter += 1
        else:
            break

draw_line()


   

s.exitonclick()