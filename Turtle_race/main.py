from turtle import Turtle, Screen
import random
screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y = -70
is_bet_on = False

all_turtles = []
for i in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(-240, y)
    all_turtles.append(new_turtle)
    y += 30
print(all_turtles)
if user_bet:
    is_bet_on = True

while is_bet_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_bet_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        rand_distance = random.randint(0, 10)
        turtle.fd(rand_distance)




screen.exitonclick()
