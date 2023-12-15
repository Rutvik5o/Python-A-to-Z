from turtle import Turtle,Screen,exitonclick

screen=Screen()

tom=Turtle()

def up():

    tom.setheading(90)  #tom.left(90)
    tom.forward(20)

def down():

    tom.setheading(270) #tom.right(90)
    tom.forward(20)

def left():

    tom.setheading(180)
    tom.forward(20)

def right():

    tom.setheading(0)
    tom.forward(20)

def Clear_Screen():

    tom.clear()
    tom.penup()
    tom.home()
    tom.pendown()


screen.listen()   #can use also turtle

screen.onkey(fun=up,key="Up")

screen.onkey(fun=down,key="Down")

screen.onkey(fun=left,key="Left")

screen.onkey(fun=right,key="Right")

screen.onkey(fun=Clear_Screen,key="c")

exitonclick()
