from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Arial', 16, 'normal')


class Scoreboard (Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.hideturtle()
        self.penup()
        self.pencolor("white")
        self.goto(x=0, y=270)
        self.print_score()

    def print_score(self):
        self.clear()
        self.write(f"score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.score += 1
        self.print_score()

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
        with open("data.txt", mode="w") as file_2:
            file_2.write(str(self.high_score))
        self.score = 0
        self.print_score()


