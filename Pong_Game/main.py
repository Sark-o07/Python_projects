from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
player_1 = Paddle((350, 0))
player_2 = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

# setting the screen attributes
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.bgcolor("black")
screen.tracer(0)

screen.listen()
screen.onkey(fun=player_1.left, key="Up")
screen.onkey(fun=player_1.right, key="Down")
screen.onkey(fun=player_2.left, key="w")
screen.onkey(fun=player_2.right, key="s")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.ball_speed)
    ball.motion()

    # detecting collision with top boundary
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detecting collision with paddle
    if ball.distance(player_1) < 50 and ball.xcor() > 320 or ball.distance(player_2) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # detecting when the ball miss the player_1
    if ball.xcor() > 390:
        ball.reset_position()
        scoreboard.l_point()

    # detecting when the ball miss the player_2
    if ball.xcor() < -390:
        ball.reset_position()
        scoreboard.r_point()





screen.exitonclick()