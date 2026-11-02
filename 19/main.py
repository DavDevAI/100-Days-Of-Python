from turtle import Screen, Turtle
import random

screen = Screen()

screen.setup(500,400)   #the width and height are NOW in fixed pixels

user_bet = screen.textinput("Your Turtle", "Choose the color of your turtle")
colors = ["red", "green", "blue", "yellow", "orange", "purple"]
start = [-225, -200] #center position to left
is_race_on = False
turtle_bank = []
for turtles in range(len(colors)):
    new_turtle = Turtle(shape = "turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtles])
    start[1] += 50
    new_turtle.goto(start[0],start[1])
    turtle_bank.append(new_turtle)


if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in turtle_bank:
        if turtle.xcor() > 225:
            is_race_on = False
            if turtle.fillcolor() == user_bet:
                print("Your Turtle wins!")
            else:
                print(f"Your Turtle lost! {turtle.fillcolor()} won")

        tloc = list(turtle.position())
        tloc[1] = random.randint(0,10)
        turtle.forward(tloc[1])


screen.exitonclick()
