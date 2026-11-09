from turtle import Turtle, Screen

screen = Screen()
screen.setup(width = 800, height = 600) # WHEN IS A LIBRARY THING AND DOESNT KNOW EXACTLY WHAT MEANS EACH MARAMETERS WE USE THE EXPLICIT PARAMETER like width = 600
screen.bgcolor("black") #changing background color and name it as black I want it black
screen.title("David´s Snake Game")

start = [0,0]
for _ in range(3):
    new_square = Turtle(shape="square")
    new_square.color("white")
    new_square.shapesize(2,2)
    start[0] += -20
    new_square.goto(start[0],0)






screen.exitonclick()

