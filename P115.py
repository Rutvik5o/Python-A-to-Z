import turtle

from turtle import Turtle,exitonclick
import random

direction=[0,90,180,270]

colors=["BlueViolet","DarkSeaGreen3","green","red","blue","orange","purple","lightblue","DeepPink3","gold4"]

turtle.colormode(255)

tom=Turtle()

tom.width(10)

tom.speed("fastest")

tom.shape("turtle")

for _ in range(100):

    r=random.randint(0,255)

    g=random.randint(0,255)

    b=random.randint(0,255)

    #tom.setheading(random.randrange(0,360,90))  #0,90,180,270

    tom.seth(random.choice(direction))

    tom.pencolor((r,g,b))

    tom.pencolor(random.choice(colors))

    tom.forward(30)

exitonclick()



