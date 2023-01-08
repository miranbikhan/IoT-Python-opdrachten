import turtle
from turtle import *
from json import load, loads

gent = '{"latitude":-4.5,"longitude":15.25,"generationtime_ms":0.6920099258422852,"utc_offset_seconds":3600,"timezone":"Africa/Kinshasa","timezone_abbreviation":"WAT","elevation":735.0,"current_weather":{"temperature":22.7,"windspeed":2.0,"winddirection":135.0,"weathercode":80,"time":1673208000},"hourly_units":{"time":"unixtime","temperature_2m":"°C"},"hourly":{"time":[1673132400,1673136000,1673139600,1673143200,1673146800,1673150400,1673154000,1673157600,1673161200,1673164800,1673168400,1673172000,1673175600,1673179200,1673182800,1673186400,1673190000,1673193600,1673197200,1673200800,1673204400,1673208000,1673211600,1673215200,1673218800,1673222400,1673226000,1673229600,1673233200,1673236800,1673240400,1673244000,1673247600,1673251200,1673254800,1673258400,1673262000,1673265600,1673269200,1673272800,1673276400,1673280000,1673283600,1673287200,1673290800,1673294400,1673298000,1673301600,1673305200,1673308800,1673312400,1673316000,1673319600,1673323200,1673326800,1673330400,1673334000,1673337600,1673341200,1673344800,1673348400,1673352000,1673355600,1673359200,1673362800,1673366400,1673370000,1673373600,1673377200,1673380800,1673384400,1673388000,1673391600,1673395200,1673398800,1673402400,1673406000,1673409600,1673413200,1673416800,1673420400,1673424000,1673427600,1673431200,1673434800,1673438400,1673442000,1673445600,1673449200,1673452800,1673456400,1673460000,1673463600,1673467200,1673470800,1673474400,1673478000,1673481600,1673485200,1673488800,1673492400,1673496000,1673499600,1673503200,1673506800,1673510400,1673514000,1673517600,1673521200,1673524800,1673528400,1673532000,1673535600,1673539200,1673542800,1673546400,1673550000,1673553600,1673557200,1673560800,1673564400,1673568000,1673571600,1673575200,1673578800,1673582400,1673586000,1673589600,1673593200,1673596800,1673600400,1673604000,1673607600,1673611200,1673614800,1673618400,1673622000,1673625600,1673629200,1673632800,1673636400,1673640000,1673643600,1673647200,1673650800,1673654400,1673658000,1673661600,1673665200,1673668800,1673672400,1673676000,1673679600,1673683200,1673686800,1673690400,1673694000,1673697600,1673701200,1673704800,1673708400,1673712000,1673715600,1673719200,1673722800,1673726400,1673730000,1673733600],"temperature_2m":[22.0,21.4,21.2,21.0,20.9,20.8,20.7,21.5,23.3,24.3,25.3,26.4,27.2,27.2,27.3,27.0,26.4,25.6,24.7,23.7,23.0,22.7,22.3,21.9,21.7,21.5,21.3,21.3,21.3,21.2,21.2,21.2,21.7,22.7,23.6,24.8,25.5,26.0,26.5,26.4,26.2,25.7,25.0,24.2,23.4,23.0,22.6,22.3,22.2,22.2,22.1,22.0,21.8,21.6,21.3,21.6,22.5,23.3,24.4,25.4,26.3,26.9,27.2,27.1,27.2,27.0,26.0,24.8,23.9,23.4,22.9,22.4,22.0,21.4,21.2,20.9,20.9,20.9,20.8,21.3,22.2,23.3,24.5,25.3,25.9,26.9,27.5,27.4,27.2,26.5,25.5,24.5,23.9,23.4,22.9,22.6,22.3,22.0,21.8,21.6,21.4,21.2,21.0,21.2,21.8,22.7,23.9,24.6,25.1,25.7,26.1,26.5,26.5,26.1,25.4,24.4,23.8,23.2,22.5,22.0,21.6,21.2,21.0,20.8,20.7,20.7,20.6,20.9,21.4,22.1,23.2,24.0,24.8,25.7,26.3,26.8,26.9,26.1,25.0,23.6,23.0,22.6,22.3,22.1,21.9,21.7,21.4,21.1,20.8,20.7,20.5,20.9,21.9,23.3,25.0,26.0,26.8,27.4,27.5,27.4,26.8,26.1,25.1,23.9,23.2,22.6,22.0,21.7]}}'

# gent = '{"latitude":55.75,"longitude":37.625,"generationtime_ms":1.2680292129516602,"utc_offset_seconds":10800,"timezone":"Europe/Moscow","timezone_abbreviation":"MSK","elevation":152.0,"current_weather":{"temperature":-16.8,"windspeed":3.6,"winddirection":276.0,"weathercode":2,"time":1673190000},"hourly_units":{"time":"unixtime","temperature_2m":"°C"},"hourly":{"time":[1673125200,1673128800,1673132400,1673136000,1673139600,1673143200,1673146800,1673150400,1673154000,1673157600,1673161200,1673164800,1673168400,1673172000,1673175600,1673179200,1673182800,1673186400,1673190000,1673193600,1673197200,1673200800,1673204400,1673208000,1673211600,1673215200,1673218800,1673222400,1673226000,1673229600,1673233200,1673236800,1673240400,1673244000,1673247600,1673251200,1673254800,1673258400,1673262000,1673265600,1673269200,1673272800,1673276400,1673280000,1673283600,1673287200,1673290800,1673294400,1673298000,1673301600,1673305200,1673308800,1673312400,1673316000,1673319600,1673323200,1673326800,1673330400,1673334000,1673337600,1673341200,1673344800,1673348400,1673352000,1673355600,1673359200,1673362800,1673366400,1673370000,1673373600,1673377200,1673380800,1673384400,1673388000,1673391600,1673395200,1673398800,1673402400,1673406000,1673409600,1673413200,1673416800,1673420400,1673424000,1673427600,1673431200,1673434800,1673438400,1673442000,1673445600,1673449200,1673452800,1673456400,1673460000,1673463600,1673467200,1673470800,1673474400,1673478000,1673481600,1673485200,1673488800,1673492400,1673496000,1673499600,1673503200,1673506800,1673510400,1673514000,1673517600,1673521200,1673524800,1673528400,1673532000,1673535600,1673539200,1673542800,1673546400,1673550000,1673553600,1673557200,1673560800,1673564400,1673568000,1673571600,1673575200,1673578800,1673582400,1673586000,1673589600,1673593200,1673596800,1673600400,1673604000,1673607600,1673611200,1673614800,1673618400,1673622000,1673625600,1673629200,1673632800,1673636400,1673640000,1673643600,1673647200,1673650800,1673654400,1673658000,1673661600,1673665200,1673668800,1673672400,1673676000,1673679600,1673683200,1673686800,1673690400,1673694000,1673697600,1673701200,1673704800,1673708400,1673712000,1673715600,1673719200,1673722800,1673726400],"temperature_2m":[-21.8,-21.5,-21.3,-21.0,-20.7,-20.4,-20.0,-19.6,-19.3,-19.4,-19.2,-18.7,-18.0,-17.3,-16.8,-14.9,-15.3,-16.0,-16.8,-17.5,-18.1,-18.8,-19.3,-19.6,-19.5,-19.4,-19.5,-19.6,-19.9,-20.8,-20.9,-20.9,-20.9,-20.8,-20.5,-19.8,-19.0,-18.2,-17.7,-17.6,-17.8,-18.2,-18.5,-18.7,-19.0,-19.3,-19.5,-19.6,-19.8,-19.9,-19.9,-20.0,-20.1,-19.9,-19.7,-19.5,-19.1,-18.7,-18.1,-17.2,-16.1,-15.2,-14.5,-14.1,-14.0,-14.0,-13.9,-13.9,-14.1,-14.3,-14.5,-14.7,-14.8,-14.9,-15.1,-15.4,-15.6,-15.6,-15.6,-15.6,-15.6,-15.6,-15.4,-15.1,-14.5,-13.8,-13.2,-12.8,-12.4,-12.1,-11.8,-11.5,-11.4,-11.2,-11.0,-10.8,-10.8,-11.1,-11.5,-11.9,-11.9,-11.8,-11.7,-11.7,-11.9,-11.8,-11.5,-10.9,-10.3,-9.9,-9.6,-9.2,-9.0,-8.8,-8.7,-8.6,-8.4,-8.3,-8.1,-7.9,-7.6,-7.5,-7.5,-7.4,-7.4,-7.3,-7.3,-7.3,-7.4,-7.4,-7.2,-6.9,-6.5,-6.2,-6.0,-5.8,-5.8,-5.7,-5.5,-5.3,-5.1,-4.9,-4.8,-4.6,-4.4,-4.2,-4.1,-3.9,-3.7,-3.6,-3.5,-3.5,-3.5,-3.4,-3.2,-2.9,-2.6,-2.5,-2.3,-2.3,-2.3,-2.5,-2.7,-2.8,-2.9,-2.9,-2.9,-2.9]}}'


# gent = '{"latitude":51.04,"longitude":3.7199998,"generationtime_ms":0.27298927307128906,"utc_offset_seconds":0,"timezone":"GMT","timezone_abbreviation":"GMT","elevation":9.0,"hourly_units":{"time":"iso8601","temperature_2m":"°C"},"hourly":{"time":["2023-01-03T00:00","2023-01-03T01:00","2023-01-03T02:00","2023-01-03T03:00","2023-01-03T04:00","2023-01-03T05:00","2023-01-03T06:00","2023-01-03T07:00","2023-01-03T08:00","2023-01-03T09:00","2023-01-03T10:00","2023-01-03T11:00","2023-01-03T12:00","2023-01-03T13:00","2023-01-03T14:00","2023-01-03T15:00","2023-01-03T16:00","2023-01-03T17:00","2023-01-03T18:00","2023-01-03T19:00","2023-01-03T20:00","2023-01-03T21:00","2023-01-03T22:00","2023-01-03T23:00","2023-01-04T00:00","2023-01-04T01:00","2023-01-04T02:00","2023-01-04T03:00","2023-01-04T04:00","2023-01-04T05:00","2023-01-04T06:00","2023-01-04T07:00","2023-01-04T08:00","2023-01-04T09:00","2023-01-04T10:00","2023-01-04T11:00","2023-01-04T12:00","2023-01-04T13:00","2023-01-04T14:00","2023-01-04T15:00","2023-01-04T16:00","2023-01-04T17:00","2023-01-04T18:00","2023-01-04T19:00","2023-01-04T20:00","2023-01-04T21:00","2023-01-04T22:00","2023-01-04T23:00","2023-01-05T00:00","2023-01-05T01:00","2023-01-05T02:00","2023-01-05T03:00","2023-01-05T04:00","2023-01-05T05:00","2023-01-05T06:00","2023-01-05T07:00","2023-01-05T08:00","2023-01-05T09:00","2023-01-05T10:00","2023-01-05T11:00","2023-01-05T12:00","2023-01-05T13:00","2023-01-05T14:00","2023-01-05T15:00","2023-01-05T16:00","2023-01-05T17:00","2023-01-05T18:00","2023-01-05T19:00","2023-01-05T20:00","2023-01-05T21:00","2023-01-05T22:00","2023-01-05T23:00","2023-01-06T00:00","2023-01-06T01:00","2023-01-06T02:00","2023-01-06T03:00","2023-01-06T04:00","2023-01-06T05:00","2023-01-06T06:00","2023-01-06T07:00","2023-01-06T08:00","2023-01-06T09:00","2023-01-06T10:00","2023-01-06T11:00","2023-01-06T12:00","2023-01-06T13:00","2023-01-06T14:00","2023-01-06T15:00","2023-01-06T16:00","2023-01-06T17:00","2023-01-06T18:00","2023-01-06T19:00","2023-01-06T20:00","2023-01-06T21:00","2023-01-06T22:00","2023-01-06T23:00","2023-01-07T00:00","2023-01-07T01:00","2023-01-07T02:00","2023-01-07T03:00","2023-01-07T04:00","2023-01-07T05:00","2023-01-07T06:00","2023-01-07T07:00","2023-01-07T08:00","2023-01-07T09:00","2023-01-07T10:00","2023-01-07T11:00","2023-01-07T12:00","2023-01-07T13:00","2023-01-07T14:00","2023-01-07T15:00","2023-01-07T16:00","2023-01-07T17:00","2023-01-07T18:00","2023-01-07T19:00","2023-01-07T20:00","2023-01-07T21:00","2023-01-07T22:00","2023-01-07T23:00","2023-01-08T00:00","2023-01-08T01:00","2023-01-08T02:00","2023-01-08T03:00","2023-01-08T04:00","2023-01-08T05:00","2023-01-08T06:00","2023-01-08T07:00","2023-01-08T08:00","2023-01-08T09:00","2023-01-08T10:00","2023-01-08T11:00","2023-01-08T12:00","2023-01-08T13:00","2023-01-08T14:00","2023-01-08T15:00","2023-01-08T16:00","2023-01-08T17:00","2023-01-08T18:00","2023-01-08T19:00","2023-01-08T20:00","2023-01-08T21:00","2023-01-08T22:00","2023-01-08T23:00","2023-01-09T00:00","2023-01-09T01:00","2023-01-09T02:00","2023-01-09T03:00","2023-01-09T04:00","2023-01-09T05:00","2023-01-09T06:00","2023-01-09T07:00","2023-01-09T08:00","2023-01-09T09:00","2023-01-09T10:00","2023-01-09T11:00","2023-01-09T12:00","2023-01-09T13:00","2023-01-09T14:00","2023-01-09T15:00","2023-01-09T16:00","2023-01-09T17:00","2023-01-09T18:00","2023-01-09T19:00","2023-01-09T20:00","2023-01-09T21:00","2023-01-09T22:00","2023-01-09T23:00"],"temperature_2m":[4.7,4.4,4.4,4.3,5.1,5.6,5.7,5.7,5.9,6.2,6.9,7.5,7.7,8.5,8.7,8.6,8.3,8.2,8.3,8.5,8.5,8.5,8.7,8.8,8.9,9.0,9.2,9.5,9.9,10.2,10.7,10.7,10.9,11.3,11.7,12.2,13.2,13.3,13.2,13.0,12.8,12.7,12.5,12.3,11.9,11.4,11.1,10.9,10.8,10.3,10.2,9.9,9.7,9.5,9.4,9.2,9.0,9.4,9.9,10.5,11.0,11.4,11.3,11.2,11.2,11.1,11.4,11.3,11.2,11.0,10.9,10.9,10.8,10.7,10.7,10.7,10.8,10.8,10.7,10.1,9.2,8.5,8.6,9.0,9.5,9.6,9.5,9.2,8.6,7.7,6.9,7.0,7.5,8.3,9.0,9.8,10.7,10.9,11.0,10.9,10.7,10.5,10.2,9.9,9.6,9.3,9.3,9.4,9.5,9.5,9.5,9.4,9.4,9.3,9.2,9.1,9.0,8.9,8.9,8.8,8.7,8.5,8.4,8.1,7.9,7.8,7.6,7.5,7.4,7.5,8.0,8.6,9.3,9.3,9.2,9.1,9.2,9.3,9.5,9.5,9.4,9.3,9.4,9.5,9.7,9.9,10.2,10.3,10.1,9.7,9.2,8.7,8.2,7.9,8.2,8.8,9.4,9.5,9.4,9.1,8.8,8.5,8.0,7.8,7.7,7.6,7.4,7.3]}}'

gentweer = loads(gent)
#all the variables needed

weer = gentweer['hourly']['temperature_2m']
weer_px = [i for i in weer]

cold = round(min(weer)) 
hot = round(max(weer))

print(cold, hot)
print('-')

total = cold - hot
print('total:', total)

steps = abs(total)

print('steps:', steps)

block = round(400/steps)
print('y_block:', block)

list_hot = hot + 1
y_axis = [*range(cold, list_hot)]

print('y axis:', y_axis)

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
def temp_y_axis():
    t.penup()
    x_start = -s.window_width() / 2 + 35
    y_start = -s.window_height() / 2 + 50   
    for y in y_axis:
        t.goto(x_start - 22, y_start)
        t.pendown()
        t.write(y, align='center', font=("Arial", 11, "normal"))
        y_start += block
        t.penup()
        # t.setheading(0)
        # t.forward(20)
        # t.write(t.pos())

temp_y_axis()
    

# for index, y in enumerate(range(cold, hot, int(steps))):
#     if index == 0:
#         t.goto(x_start - 25, y_start)
#         t.write("")
#         y_start += 40
#         continue
#     t.goto(x_start - 25 , y_start)
#     t.write(y, font=("Arial", 12, "normal"))
#     max = t.pos()
#     y_start += 40

# max_y = max[1]
# print('max_y:', max_y)

# t.penup()

def y_axis_lines():
    x_start = -s.window_width() / 2 + 35
    y_l = -275 + block + 5
    t.pencolor((226, 226, 226))
    for l in range(steps):
        t.goto(x_start, y_l)
        t.setheading(0)
        t.pendown()
        t.forward(970)
        t.penup()
        y_l += block

y_axis_lines()


x_start = -s.window_width() / 2 + 35
y_start = -s.window_height() / 2 + 50
t.color('black')

# x-as
t.penup()
t.goto(x_start, y_start + 5)
# t.write(t.pos())
t.setheading(0)
t.pendown()
t.forward(970)
t.penup()

def x_days():
    x_start = -s.window_width() / 2 + 45
    y_start = -s.window_height() / 2 + 50
    for d in range(4):
            t.goto(x_start, y_start + 4)
            t.write(t.pos())
            t.setheading(-90)
            t.pendown()
            t.pensize(2)
            t.forward(20)
            t.penup()
            t.forward(20)
            t.setheading(0)
            t.write('day', True, align="center", font=("Arial", 14, 'normal'))
            x_start += 240

x_days()

def x_noon():
    x_start = -s.window_width() / 2 + 165
    y_start = -s.window_height() / 2 + 50
    for d in range(4):
            t.pensize(0)
            t.goto(x_start, y_start + 4)
            t.setheading(-90)
            t.pendown()
            t.forward(20)
            t.penup()
            t.forward(20)
            t.setheading(0)
            t.write('12:00', True, align="center")
            x_start += 240
x_noon()

def x_2h():
    x_start = -s.window_width() / 2 + 65
    y_start = -s.window_height() / 2 + 50
    for h in range(48):
            t.pensize(0)
            t.goto(x_start, y_start + 4)
            t.setheading(-90)
            t.pendown()
            t.forward(10)
            t.penup()
            x_start += 20

x_2h()


# x_start = -s.window_width() / 2 + 35
# y_start = -s.window_height() / 2 + 50
    

# def start_pos_weath_line():
#     t.penup()
#     draw_sx = -580
#     draw_sy = -275
#     print('draw_sy:', draw_sy)
#     t.goto(draw_sx, draw_sy)
#     t.write('max')
#     t.write(t.pos())
# start_pos_weath_line()

draw_sx = -580
draw_sy = -275

def draw_line():
    t.penup()
    draw_sx = -580
    draw_sy = -275
    print('draw_sy:', draw_sy)
    t.goto(draw_sx, draw_sy)
    t.write('max')
    t.write(t.pos())
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
            print(counter)
        else:
            break

draw_line()


   

s.exitonclick()