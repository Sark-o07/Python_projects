import turtle as t
import random


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


tim = t.Turtle()
t.colormode(255)
tim.speed("fastest")


def draw_spirogragh(offset):
    for _ in range(int(360/offset)):
        tim.color(random_color())
        tim.circle(120)
        tim.setheading(tim.heading() + offset)


draw_spirogragh(3)


#
#
# angle = [0, 90, 180, 270]
# timmy_the_turtle.width(8)
# timmy_the_turtle.speed(0)
# for _ in range(200):
#     timmy_the_turtle.forward(20)
#     timmy_the_turtle.seth(random.choice(angle))
#     timmy_the_turtle.color(random_color())


screen = t.Screen()
screen.exitonclick()
