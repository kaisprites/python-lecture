import turtle
import threading
from math import *


class Star:
    my_turtle = None
    line = 0
    density = 0

    def __init__(self, line, density):
        self.my_turtle = turtle.Turtle('turtle')
        self.my_turtle.speed(3)
        self.my_turtle.pensize(1)
        self.line = line
        self.density = density
        print(f"turtle ({line}, {density}) is created")

    def draw_shape(self):
        print(f"draw shape: ({self.line}, {self.density})")
        self.my_turtle.penup()
        theta = pi * self.density * 2 / self.line
        theta_starter = pi * 2 / self.line

        for j in range(0, gcd(self.line, self.density)):
            c = theta_starter * j
            self.my_turtle.goto(cos(c) * 300, sin(c) * 300)
            self.my_turtle.pendown()
            for i in range(0, (self.line // gcd(self.line, self.density)) + 1):
                self.my_turtle.goto(cos(theta * i + c) * 300, sin(theta * i + c) * 300)
            self.my_turtle.penup()

        self.my_turtle.goto(0, 0)


def turtle_star_thread(line, density):
    print(f"turtle star thread: ({line}, {density})")
    star = Star(line, density)
    star.draw_shape()

def turtle_star(line, density=None):
    if density is None:
        for i in range(1, ceil(line / 2)):
            turtle_star(line, i)
        return

    threading.Thread(target=turtle_star_thread, args=(line, density)).start()


turtle_star(7)
turtle.done()
