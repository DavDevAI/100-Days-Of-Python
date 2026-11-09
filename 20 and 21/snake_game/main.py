from turtle import Screen, Turtle
from snake import Snake
import time

screen = Screen()
screen.setup(width = 800, height = 600) # WHEN IS A LIBRARY THING AND DOESN'T KNOW EXACTLY WHAT MEANS EACH pARAMETERS WE USE THE EXPLICIT PARAMETER like width = 600
screen.bgcolor("black") #changing background color and name it as black I want it black
screen.title("David´s Snake Game")
screen.tracer(0)
screen.listen()

snake = Snake()
snake.initialize_snake()
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()




screen.exitonclick()