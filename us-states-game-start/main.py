import turtle
import pandas as pd

data = pd.read_csv("50_states.csv")
print(data.state)
screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)
title = "Guess the State"
is_game_on = True
count = 0
guessed_state = []
while is_game_on:
    answer_state = screen.textinput(title=title, prompt="what's another state name: ").title()

    if count == 50 or answer_state == "Exit":
        is_game_on = False
        break

    for state in data.state:
        if state == answer_state:
            guessed_state.append(answer_state)
            screen.tracer(0)
            tim = turtle.Turtle()
            tim.penup()
            tim.hideturtle()
            screen.update()
            state_row = data[data.state == state]
            state_xcor = float(state_row.x)
            state_ycor = float(state_row.y)
            tim.goto(state_xcor, state_ycor)
            tim.write(state, align="center", font=("Courier", 6, "normal"))
            count += 1
        title = f"{count}/50 States Correct"
missed_state = [state for state in data.state if state not in guessed_state]
print(guessed_state)
print(missed_state)
new_data = pandas.DataFrame(missed_state)
new_data.to_csv("missing_state.csv")








# print(Texas.state)
# print(data.index)
# oyo = Texas.index
# print(oyo)
# state_dict = Texas.to_dict()
# print(state_dict)
# print(state_dict['state'])
# if data[data.state == var]:
#     print("yeah")
# else:
#     print("yar")




screen.exitonclick()
