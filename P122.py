#Sketch

from turtle import Turtle,Screen

tom=Turtle()

screen=Screen()

def move_forward():
    tom.forward(10)

def move_backward():
    tom.backward(10)

def turn_left():
    new_heading=tom.heading() + 20
    tom.setheading(new_heading)
    tom.forward(10)

def turn_right():

    new_heading=tom.heading() - 20
    tom.setheading(new_heading)
    tom.forward(10)

def Clear_Screen():

    tom.clear()
    tom.penup()
    tom.home()
    tom.pendown()

screen.listen()

screen.onkey(fun=move_forward,key="f")

screen.onkey(fun=move_backward,key="b")

screen.onkey(fun=turn_left,key="l")

screen.onkey(fun=turn_right,key="r")

screen.onkey(fun=Clear_Screen,key="c")

screen.exitonclick()











