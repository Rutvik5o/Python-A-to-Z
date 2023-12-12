from turtle import Turtle,Screen,exitonclick

tom=Turtle()

s1=Screen()


tom.color("red","green")

tom.begin_fill()

print(tom.heading())

tom.speed(8)

while True:

    tom.forward(200)
    tom.left(170)
    if tom.heading()==0:
        break

tom.end_fill()
s1.exitonclick()