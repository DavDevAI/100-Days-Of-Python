from turtle import Turtle
LEFT_COORDS = (-300,0)
RIGHT_COORDS = (300,0)
MOVE_DISTANCE = 20
UP = 90
DOWN = 270

class Paddle:
    def __init__(self):
        #self.paddle_segments = []
        self.initialize_paddle(LEFT_COORDS)
        #self.right_paddle = self.initialize_paddle(RIGHT_COORDS)
        #self.head = self.paddle_segments[0]

    def initialize_paddle(self, COORDS):
        # for position in STARTING_POSITIONS:
        #     self.build_paddle(position)
        new_paddle = Turtle(shape="square")
        new_paddle.color("white")
        new_paddle.shapesize(stretch_wid=3, stretch_len=1)
        new_paddle.penup()
        new_paddle.goto(COORDS)
        #self.paddle_segments.append(new_paddle)

    # def build_paddle(self, position):
    #     new_paddle = Turtle(shape="square")
    #     new_paddle.color("white")
    #     new_paddle.penup()
    #     new_paddle.goto(position)
    #     self.paddle_segments.append(new_paddle)
    #
    # def move_paddle(self):
    #     #reversed_segments = self.paddle_segments[::-1]
    #     for seg_index in range(len(self.paddle_segments)-1, 0, -1):
    #     #for seg_index in range(len(reversed_segments)):
    #         new_x = self.paddle_segments[seg_index - 1].xcor()
    #         new_y = self.paddle_segments[seg_index - 1].ycor()
    #         self.paddle_segments[seg_index].goto(new_x, new_y)
    #     self.head.forward(MOVE_DISTANCE)

    def paddle_up(self ):
        self.setheading(UP)
        self.forward(MOVE_DISTANCE)

    def paddle_down(self):
        self.setheading(UP)
        self.forward(MOVE_DISTANCE)