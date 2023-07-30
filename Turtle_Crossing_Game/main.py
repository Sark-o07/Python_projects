from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import time

screen = Screen()
screen.title("Crossing Game")
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
player = Player()
screen.onkey(fun=player.move_forward, key="Up")
car_manager = CarManager()
scoreboard = Scoreboard()

is_game_on = True

while is_game_on:
    time.sleep(0.1)

    screen.update()
    car_manager.create_car()
    car_manager.move_horizontally()

    # detect car collision with player
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            is_game_on = False
            scoreboard.game_over()

    if player.ycor() > 260:
        scoreboard.add_point()
        player.reset_position()
        car_manager.level_up()













screen.exitonclick()




























screen.exitonclick()