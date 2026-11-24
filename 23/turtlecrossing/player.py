from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("black")
        #self.speed("fastest")
        self.goto(0, -270)
        self.setheading(90)

    def move_up(self):
        self.sety(self.ycor() + MOVE_DISTANCE)
