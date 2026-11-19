from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

LEFT_COORDS = (-300,0)
RIGHT_COORDS = (300,0)

screen = Screen()
screen.setup(width = 800, height = 600)
screen.bgcolor("black")
screen.title("David´s PONG")
screen.tracer(0)
screen.listen()


paddle_left = Paddle(LEFT_COORDS)
paddle_right = Paddle(RIGHT_COORDS)

ball = Ball(paddle_left, paddle_right)

screen.onkeypress(key="w", fun=paddle_left.paddle_up)
screen.onkeypress(key="s", fun=paddle_left.paddle_down)

screen.onkeypress(key="Up", fun=paddle_right.paddle_up)
screen.onkeypress(key="Down", fun=paddle_right.paddle_down)


game_is_on = True

while game_is_on:

    screen.update()
    time.sleep(0.042)
    ball.bounce_physics()



screen.exitonclick()