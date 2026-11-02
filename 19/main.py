from turtle import Screen, Turtle
import random

screen = Screen()

screen.setup(500,400)   #the width and height are NOW in fixed pixels

user_bet = screen.textinput("Your Turtle", "Choose the color of your turtle")
colors = ["red", "green", "blue", "yellow", "orange", "purple"]
start = [-225, -200] #center position to left
is_race_on = False
position_bank = []
turtle_bank = []
for turtles in range(len(colors)):
    tim = Turtle(shape = "turtle")
    tim.penup()
    tim.color(colors[turtles])
    start[1] += 50
    tim.goto(start[0],start[1])
    turtle_bank.append(tim)
    position_bank.append(list(tim.position()))

print(position_bank)
if is_race_on:
    is_race_on = True

while is_race_on:
    random.randint(0,10)


screen.exitonclick()
