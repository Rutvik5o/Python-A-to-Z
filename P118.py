import random

import turtle

from turtle import Turtle,Screen

tom=Turtle()

turtle.colormode(255)

s1=Screen()

print(s1.screensize())

tom.penup()

tom.speed(10)

color_list=[(246,2,211),(132,123,135),(122,187,99),(122,101,200),(50,144,212),(90,190,219)]

for _ in range(300):

    tom.pencolor(random.choice(color_list))

    tom.goto(random.randint(-300,300),random.randint(-300,300))

    tom.dot()

s1.exitonclick()