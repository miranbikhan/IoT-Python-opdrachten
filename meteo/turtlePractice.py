from turtle import *

height = 720
width = 1024

setup(width, height)



setworldcoordinates(-20, -20, 200, 200)
colormode(255)
color((211, 211, 211))

lines = 0
speed(3)


penup()
left(-180)
forward(10)
left(-90)

for x in range(8):
    write('-10')
    penup()
    forward(20)

setpos(-10, -10)

right(90)
pendown()
forward(100)


# while lines < 8:
#     setworldcoordinates(-20, -20, 200, 200)
#     write('hello')
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
#     lines += 2



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
 