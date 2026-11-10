from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
STARTING_POSITIONS = [(0,0), (0,-20), (0,-40)]

class Snake:

    def __init__(self):
        #self.start = [0, 0] Not used anymore
        self.segments = []
        self.initialize_snake()
        self.head = self.segments[0]

    def initialize_snake (self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)
        #previous legacy implementation
        # for _ in range(3):
        #     new_square = Turtle(shape="square")
        #     new_square.color("white")
        #     new_square.penup()
        #     self.start[0] += -20
        #     new_square.goto(self.start[0], 0)
        #     self.segments.append(new_square)

    def add_segment(self, position):
        new_square = Turtle(shape="square")
        new_square.color("white")
        new_square.penup()
        new_square.goto(position)
        self.segments.append(new_square)

    def increase_tail(self):
        #add a segment to the snake
        self.add_segment(self.segments[-1].position())

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

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):  #also could reverse creating a new list variable and slicing and rearranging reversed = self.segments[::-1]
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANCE)
