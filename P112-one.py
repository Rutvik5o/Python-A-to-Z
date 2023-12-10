from turtle import Turtle,exitonclick

tom=Turtle()

tom.shape("turtle")

tom.color("blue","pink")

tom.begin_fill()

tom.circle(100)

tom.end_fill()

tom.rt(90)

tom.penup()

print(tom.isdown())

tom.forward(100)

tom.pendown()

tom.pensize(5)

tom.circle(50)

print(tom.pos())

tom.goto(-100,-100)

tom.showturtle

exitonclick()
