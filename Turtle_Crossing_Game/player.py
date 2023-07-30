from turtle import Turtle
FORWARD_PACE = 5


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.reset_position()
        self.setheading(90)

    def move_forward(self):
        self.fd(FORWARD_PACE)

    def reset_position(self):
        self.goto(0, -280)


