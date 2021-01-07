import turtle
import threading
from math import *


def call1(x, y):
    print(x, y)


turtle.title('거북이')
colors = ['red', 'green', 'blue']

# my = turtle.Turtle('turtle')
#
# my.pensize(10)
# my.pencolor('black')
# turtle.onscreenclick(call1, 1)
#
# my.penup()
# my.goto(-200,0)
# my.pendown()
# for i in range(-200,201):
#     my.goto(i, (200**2 - i**2)**0.5)
#     if i%20 == 0:
#         my.pencolor(colors[(i//20)%len(colors)])
# for i in range(200,-201,-1):
#     my.goto(i, -((200**2 - i**2)**0.5))
#     if i%20 == 0:
#         my.pencolor(colors[(i//20)%len(colors)])
# my.penup()
# my.goto(0,0)

evil = turtle.Turtle('turtle')
evil.speed(10)

evil.pensize(1)
evil.penup()


def turtlestar(line, density=None):
    if density is None:
        for i in range(1, ceil(line / 2)):
            evil.pencolor(colors[(i-1)%len(colors)])
            turtlestar(line, i)
        return

    theta = pi*density*2/line
    theta_starter = pi*2/line

    for j in range(0, gcd(line,density)):
        c = theta_starter * j
        evil.goto(cos(c)*300, sin(c)*300)
        evil.pendown()
        for i in range(0, (line//gcd(line,density))+1):
            evil.goto(cos(theta*i+c)*300, sin(theta*i+c)*300)
        evil.penup()


turtlestar(1)
evil.goto(0,0)

turtle.done()
