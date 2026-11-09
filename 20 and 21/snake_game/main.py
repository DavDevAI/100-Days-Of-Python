from turtle import Screen
from snake import Snake
import time

screen = Screen()
screen.setup(width = 800, height = 600) # WHEN IS A LIBRARY THING AND DOESN'T KNOW EXACTLY WHAT MEANS EACH pARAMETERS WE USE THE EXPLICIT PARAMETER like width = 600
screen.bgcolor("black") #changing background color and name it as black I want it black
screen.title("David´s Snake Game")
screen.tracer(0)
screen.listen()

snake = Snake()

#movements #here I use onkey because if I use onkeypress() and will continue to call the movement and translates on accelerating the snake and
#for the logics of this games acceleration is not allowed

screen.onkey(key="Up", fun=snake.move_up)
screen.onkey(key="Down", fun=snake.move_down)
screen.onkey(key="Left", fun=snake.move_left)
screen.onkey(key="Right", fun=snake.move_right)

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()


screen.exitonclick()