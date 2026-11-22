from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270

class Paddle(Turtle):
    def __init__(self, coords):
        #self.paddle_segments = []
        super().__init__()
        self.coords = coords
        self.initialize_paddle(coords)
        self.dx = 5
        self.dy = -5
        #self.head = self.paddle_segments[0]

    def initialize_paddle(self, coords):
        # for position in STARTING_POSITIONS:
        #     self.build_paddle(position)
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=4, stretch_len=1)
        self.penup()
        self.goto(coords)
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
        # self.setx(self.xcor() + MOVE_DISTANCE)
        # self.sety(self.ycor() + MOVE_DISTANCE)
        #WE DO THIS IF WE WANT A MIXED COMPONENT OF X AND Y LIKE THE BALL LIKE A DERIVE or a component of x+y for this case only y
        self.sety(self.ycor() + MOVE_DISTANCE) #IN THIS CASE IF WE ONLY WANT TO MOVE UP AND DOWN THAT MEANS ONLY IN Y
        #SO FROM THE DERIVE OR COMPONENT ONLY EXTRACT THE Y COMPONENT AND THEN just move on Y, also taken from the logic of the sample code of
        # y = left_pad.ycor()
        # if y < 250:  # Limit paddle movement
        #     y += 20
        #     left_pad.sety(y)
        #later we could add restriction on x
    def paddle_down(self):
        #self.setx(self.xcor() + -20)
        self.sety(self.ycor() + -(MOVE_DISTANCE))