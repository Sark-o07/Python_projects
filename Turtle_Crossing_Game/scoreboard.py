from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 23, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.hideturtle()
        self.penup()
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-235, 270)
        self.write(f"Level: {self.level}", align=ALIGNMENT, font=FONT)

    def add_point(self):
        self.level += 1
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)








