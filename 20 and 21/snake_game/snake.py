from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.start = [0, 0]
        self.segments = []
        self.initialize_snake()
        self.head = self.segments[0]

    def initialize_snake (self):
        for _ in range(3):
            new_square = Turtle(shape="square")
            new_square.color("white")
            new_square.penup()
            self.start[0] += -20
            new_square.goto(self.start[0], 0)
            self.segments.append(new_square)

    def move_up(self):
        #CONDITIONAL TO AVOID TURNING BACK ON ITS OWN TAIL
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def move_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def move_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def move_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    #self.initialize_snake()
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANCE)

