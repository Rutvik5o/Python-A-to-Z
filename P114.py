import random
from turtle import Turtle,exitonclick

tom=Turtle()

colors=["BlueViolet","DarkSeaGreen3","green","red","blue","orange","purple","lightblue","DeepPink3","gold4"]

for i in range(3,9):

    angle=360/i;
    tom.pencolor(random.choice(colors))

    for _ in range(i):

        tom.forward(100)

        tom.right (angle)

exitonclick()

