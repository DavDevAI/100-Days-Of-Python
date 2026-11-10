from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width = 600, height = 600) # WHEN IS A LIBRARY THING AND DOESN'T KNOW EXACTLY WHAT MEANS EACH pARAMETERS WE USE THE EXPLICIT PARAMETER like width = 600
screen.bgcolor("black") #changing background color and name it as black I want it black
screen.title("David´s Snake Game")
screen.tracer(0)
screen.listen()

snake = Snake()
food = Food()
scoreboard = Scoreboard()

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

    #Detect collision with food
    #using .distance() method
    if snake.head.distance(food) < 16: #for this method I can compare if an object is at a certain distance from another object in this case food so I pass as a parameter "food"
        print("eating")
        scoreboard.increase_score()
        food.refresh_food()
        snake.increase_tail()

    #Detect collision with the walls to end the game
    if snake.head.xcor() > 280 or snake.head.ycor() > 280 or snake.head.xcor() < -280 or snake.head.ycor()<-280:
        game_is_on = False
        scoreboard.game_over()




screen.exitonclick()