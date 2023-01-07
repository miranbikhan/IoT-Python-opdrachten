from turtle import *
from json import load, loads

gent = '{"latitude":51.04,"longitude":3.7199998,"generationtime_ms":0.27298927307128906,"utc_offset_seconds":0,"timezone":"GMT","timezone_abbreviation":"GMT","elevation":9.0,"hourly_units":{"time":"iso8601","temperature_2m":"°C"},"hourly":{"time":["2023-01-03T00:00","2023-01-03T01:00","2023-01-03T02:00","2023-01-03T03:00","2023-01-03T04:00","2023-01-03T05:00","2023-01-03T06:00","2023-01-03T07:00","2023-01-03T08:00","2023-01-03T09:00","2023-01-03T10:00","2023-01-03T11:00","2023-01-03T12:00","2023-01-03T13:00","2023-01-03T14:00","2023-01-03T15:00","2023-01-03T16:00","2023-01-03T17:00","2023-01-03T18:00","2023-01-03T19:00","2023-01-03T20:00","2023-01-03T21:00","2023-01-03T22:00","2023-01-03T23:00","2023-01-04T00:00","2023-01-04T01:00","2023-01-04T02:00","2023-01-04T03:00","2023-01-04T04:00","2023-01-04T05:00","2023-01-04T06:00","2023-01-04T07:00","2023-01-04T08:00","2023-01-04T09:00","2023-01-04T10:00","2023-01-04T11:00","2023-01-04T12:00","2023-01-04T13:00","2023-01-04T14:00","2023-01-04T15:00","2023-01-04T16:00","2023-01-04T17:00","2023-01-04T18:00","2023-01-04T19:00","2023-01-04T20:00","2023-01-04T21:00","2023-01-04T22:00","2023-01-04T23:00","2023-01-05T00:00","2023-01-05T01:00","2023-01-05T02:00","2023-01-05T03:00","2023-01-05T04:00","2023-01-05T05:00","2023-01-05T06:00","2023-01-05T07:00","2023-01-05T08:00","2023-01-05T09:00","2023-01-05T10:00","2023-01-05T11:00","2023-01-05T12:00","2023-01-05T13:00","2023-01-05T14:00","2023-01-05T15:00","2023-01-05T16:00","2023-01-05T17:00","2023-01-05T18:00","2023-01-05T19:00","2023-01-05T20:00","2023-01-05T21:00","2023-01-05T22:00","2023-01-05T23:00","2023-01-06T00:00","2023-01-06T01:00","2023-01-06T02:00","2023-01-06T03:00","2023-01-06T04:00","2023-01-06T05:00","2023-01-06T06:00","2023-01-06T07:00","2023-01-06T08:00","2023-01-06T09:00","2023-01-06T10:00","2023-01-06T11:00","2023-01-06T12:00","2023-01-06T13:00","2023-01-06T14:00","2023-01-06T15:00","2023-01-06T16:00","2023-01-06T17:00","2023-01-06T18:00","2023-01-06T19:00","2023-01-06T20:00","2023-01-06T21:00","2023-01-06T22:00","2023-01-06T23:00","2023-01-07T00:00","2023-01-07T01:00","2023-01-07T02:00","2023-01-07T03:00","2023-01-07T04:00","2023-01-07T05:00","2023-01-07T06:00","2023-01-07T07:00","2023-01-07T08:00","2023-01-07T09:00","2023-01-07T10:00","2023-01-07T11:00","2023-01-07T12:00","2023-01-07T13:00","2023-01-07T14:00","2023-01-07T15:00","2023-01-07T16:00","2023-01-07T17:00","2023-01-07T18:00","2023-01-07T19:00","2023-01-07T20:00","2023-01-07T21:00","2023-01-07T22:00","2023-01-07T23:00","2023-01-08T00:00","2023-01-08T01:00","2023-01-08T02:00","2023-01-08T03:00","2023-01-08T04:00","2023-01-08T05:00","2023-01-08T06:00","2023-01-08T07:00","2023-01-08T08:00","2023-01-08T09:00","2023-01-08T10:00","2023-01-08T11:00","2023-01-08T12:00","2023-01-08T13:00","2023-01-08T14:00","2023-01-08T15:00","2023-01-08T16:00","2023-01-08T17:00","2023-01-08T18:00","2023-01-08T19:00","2023-01-08T20:00","2023-01-08T21:00","2023-01-08T22:00","2023-01-08T23:00","2023-01-09T00:00","2023-01-09T01:00","2023-01-09T02:00","2023-01-09T03:00","2023-01-09T04:00","2023-01-09T05:00","2023-01-09T06:00","2023-01-09T07:00","2023-01-09T08:00","2023-01-09T09:00","2023-01-09T10:00","2023-01-09T11:00","2023-01-09T12:00","2023-01-09T13:00","2023-01-09T14:00","2023-01-09T15:00","2023-01-09T16:00","2023-01-09T17:00","2023-01-09T18:00","2023-01-09T19:00","2023-01-09T20:00","2023-01-09T21:00","2023-01-09T22:00","2023-01-09T23:00"],"temperature_2m":[4.7,4.4,4.4,4.3,5.1,5.6,5.7,5.7,5.9,6.2,6.9,7.5,7.7,8.5,8.7,8.6,8.3,8.2,8.3,8.5,8.5,8.5,8.7,8.8,8.9,9.0,9.2,9.5,9.9,10.2,10.7,10.7,10.9,11.3,11.7,12.2,13.2,13.3,13.2,13.0,12.8,12.7,12.5,12.3,11.9,11.4,11.1,10.9,10.8,10.3,10.2,9.9,9.7,9.5,9.4,9.2,9.0,9.4,9.9,10.5,11.0,11.4,11.3,11.2,11.2,11.1,11.4,11.3,11.2,11.0,10.9,10.9,10.8,10.7,10.7,10.7,10.8,10.8,10.7,10.1,9.2,8.5,8.6,9.0,9.5,9.6,9.5,9.2,8.6,7.7,6.9,7.0,7.5,8.3,9.0,9.8,10.7,10.9,11.0,10.9,10.7,10.5,10.2,9.9,9.6,9.3,9.3,9.4,9.5,9.5,9.5,9.4,9.4,9.3,9.2,9.1,9.0,8.9,8.9,8.8,8.7,8.5,8.4,8.1,7.9,7.8,7.6,7.5,7.4,7.5,8.0,8.6,9.3,9.3,9.2,9.1,9.2,9.3,9.5,9.5,9.4,9.3,9.4,9.5,9.7,9.9,10.2,10.3,10.1,9.7,9.2,8.7,8.2,7.9,8.2,8.8,9.4,9.5,9.4,9.1,8.8,8.5,8.0,7.8,7.7,7.6,7.4,7.3]}}'

gentweer = loads(gent)

time = [*range(0, 1210, 10)]

# print(time)
weer = gentweer['hourly']['temperature_2m']
weer_px = [i * 40  for i in weer]

combo = dict(zip(time, weer_px))

# cold = min(weer)
# hot = max(weer)
# print(cold)
# print(hot)

setup(1250, 850)

setworldcoordinates(-50, -50, 1250, 850)
draw_pos = (0, weer_px[0])
# x-as = 5 x 24 uur x 10
# y-as = 8 temps x 100

speed(8)
delay(0)
# ht()

penup()
goto(-40, 0)
setheading(90)

y_as = range(2, 18, 2)
for x in y_as:
    pensize(3)
    write(x)
    penup()
    forward(100)
# y-as met temperatuurwaarden


penup()
setpos(0, 0)
setheading(0)

pensize(0)
pencolor('grey')

up = 5
for l in range(8):
    setpos(0, up)
    pendown()
    forward(1200)
    penup()
    up += 100
# temperatuurslijnen


# penup()
# # goto(draw_pos)
# setpos(0, 5)
# setheading(0)
# pencolor('blue')
# setheading(90)
# pendown()
# forward(100)

penup()
setpos(time[0], weer_px[0])

for d, r in combo.items():
    # penup()
    # pensize(2)
    # setheading(towards(d, r))
    # pendown()
    # dot()
    # forward(10)
    setpos(d, r)
    pendown()
    pensize(2)
    dot()




exitonclick()