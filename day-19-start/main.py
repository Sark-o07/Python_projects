from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def forward():
    tim.fd(20)


def backward():
    tim.back(20)


def turn_right():
     tim.right(20)


def turn_left():
    tim.left(20)


def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkey(key="w", fun=forward)
screen.onkey(key="s", fun=backward)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear)

screen.exitonclick()