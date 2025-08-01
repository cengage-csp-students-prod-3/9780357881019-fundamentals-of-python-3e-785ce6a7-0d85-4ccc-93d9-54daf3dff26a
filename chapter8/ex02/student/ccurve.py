"""
Program file: ccurve.py

This program prompts the user for the level of
a c-curve and draws a c-curve of that level.
"""

from turtle import Turtle, tracer, update

import turtle
import random

# List of colors to choose from
colors = ['red', 'green', 'blue', 'purple', 'orange', 'yellow', 'cyan', 'magenta']

def c_curve(t, order, size, sign=1):
    if order == 0:
        t.color(random.choice(colors))  # Pick a random color for this line segment
        t.forward(size)
    else:
        t.right(sign * 45)
        c_curve(t, order - 1, size / (2 ** 0.5), 1)
        t.left(sign * 90)
        c_curve(t, order - 1, size / (2 ** 0.5), -1)
        t.right(sign * 45)

def main():
    screen = turtle.Screen()
    screen.bgcolor('white')
    t = turtle.Turtle()
    t.speed(0)  # Fastest
    t.penup()
    t.goto(-200, 0)
    t.pendown()

    order = 7
    size = 400

    c_curve(t, order, size)

    screen.mainloop()

if __name__ == "__main__":
    main()
