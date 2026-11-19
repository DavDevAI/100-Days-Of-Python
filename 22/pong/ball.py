from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        # as I am inheriting from the Turtle I don't need and object and directly can pull Turtle's methods
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=.5,
                       stretch_len=.5)  # stretching by .5 that means by its half, it was 20 by 20, now is 10 by 10
        self.color("white")
        self.speed("fastest")
        self.goto(0,0)
        self.dx = 5
        self.dy = -5
        self.bounce()

    def bounce(self):
        self.setx(self.xcor() + self.dx)
        self.sety(self.ycor() + self.dy)

        #bouncing borders JUST TOP AND BOTTOM
        # Checking borders
        if self.ycor() > 280:
            self.sety(280)
            self.dy *= -1

        if self.ycor() < -280:
            self.sety(-280)
            self.dy *= -1