import turtle as t
import random

rgb_colors =\
    [
              (176, 48, 79), (42, 98, 146), (205, 161, 94), (223, 210, 102), (137, 90, 64), (177, 164, 38),
              (109, 176, 207), (212, 131, 173), (227, 73, 49), (201, 75, 117), (88, 105, 192), (28, 143, 89),
              (124, 218, 207), (120, 43, 71), (94, 158, 65), (227, 170, 187), (131, 184, 161), (48, 187, 202),
              (172, 187, 222), (232, 173, 164), (154, 209, 219), (100, 51, 43), (34, 64, 115), (44, 80, 79),
              (215, 207, 37), (52, 58, 66), (31, 87, 90), (76, 51, 43), (40, 67, 65), (84, 37, 55)
    ]

tim = t.Turtle()
t.colormode(255)
tim.penup()
tim.setheading(225)
tim.fd(300)
tim.setheading(0)

def movement():
    for _ in range(9):

        tim.dot(20, random.choice(rgb_colors))
        tim.fd(50)
        tim.dot(20, random.choice(rgb_colors))


def turn_left():
    tim.setheading(90)
    tim.fd(50)
    tim.setheading(180)


def turn_right():
    tim.setheading(90)
    tim.fd(50)
    tim.setheading(0)


for _ in range(5):
    movement()
    turn_left()
    movement()
    turn_right()



















screen = t.Screen()
screen.exitonclick()



