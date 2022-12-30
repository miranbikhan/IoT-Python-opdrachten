from turtle import *



height = 720
width = 1400


setup(width, height)

setworldcoordinates(-20, -20, 200, 200)
colormode(255)
# hideturtle()

speed(3)


penup()
left(-180)
forward(10)
left(-90)

temperatures = range(-6, 10, 2)
for x in temperatures:
    write(x)
    penup()
    forward(20)

setpos(-10, -10)

right(180)
forward(10)
left(90)
forward(10)

time = ['00:00', '01:00', '02:00', '03:00', '04:00', '05:00', '06:00', '07:00', '08:00', '09:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00', '21:00', '22:00', '23:00']
for y in time[::2]:
    write(y)
    forward(15)


color((211, 211, 211))



# hoe ik die code hieronder heb gefixt, ziek of ni?
up = 2
for l in range(8):
    setpos(-5, up)
    pendown()
    forward(180)
    penup()
    up += 20







# setpos(-5, -18)
# left(90)
# forward(20)
# left(-90)
# pendown()
# forward(180)

# for l in range(3):
#     penup()
#     left(90)
#     forward(20)
#     left(90)
#     pendown()
#     forward(180)
#     penup()
#     right(90)
#     forward(20)
#     right(90)
#     pendown()
#     forward(180)



# for l in range(4):
#     forward(180)
#     penup()
#     left(90)
#     forward(20)
#     left(90)
#     pendown()
#     forward(180)
#     penup()
#     left(-90)
#     forward(20)
#     left(-90)
#     pendown()



# penup()
# goto(-20, -20)
# forward(0)
# left(-90)
# pendown()
# forward(5)
# penup()
# forward(5)
# write('12 Dec')



# left(-90)
# forward(180)
# left(90)
# penup()
# forward(10)
# pendown()
# left(90)
# forward(180)
# pendown()
# left(-90)
# penup()
# forward(10)
# pendown()
# left(-90)
# forward(180)


done()
 