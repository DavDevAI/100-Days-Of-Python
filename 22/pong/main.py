import time
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("David´s PONG")
screen.tracer(0)
screen.listen()

#screen.update()
paddle = Paddle()
ball = Ball()

screen.onkeypress(key="Up", fun=paddle.paddle_up)
screen.onkeypress(key="Down", fun=paddle.paddle_down)


game_is_on = True

while game_is_on:

    screen.update()
    time.sleep(0.1)
    ball.bounce()



screen.exitonclick()