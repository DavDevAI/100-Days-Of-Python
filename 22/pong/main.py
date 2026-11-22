from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

LEFT_COORDS = (-325,0)
RIGHT_COORDS = (325,0)

screen = Screen()
screen.setup(width = 800, height = 600)
screen.bgcolor("black")
screen.title("David´s PONG")
screen.tracer(0)
screen.listen()


paddle_left = Paddle(LEFT_COORDS)
score_left = Scoreboard((-200, 270))
paddle_right = Paddle(RIGHT_COORDS)
score_right = Scoreboard((200, 270))
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

    if ball.xcor() > 400:
        score_left.increase_score()
        ball.reset_position()
        paddle_left.reset_position()
        paddle_right.reset_position()
    if ball.xcor() < -400:
        score_right.increase_score()
        ball.reset_position()
        paddle_left.reset_position()
        paddle_right.reset_position()

screen.exitonclick()