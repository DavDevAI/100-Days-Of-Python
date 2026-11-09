from turtle import Screen, Turtle

screen = Screen()
screen.listen()



class Snake:

    def __init__(self):
        self.start = [0, 0]
        self.segments = []

    def initialize_snake (self):
        for _ in range(3):
            new_square = Turtle(shape="square")
            new_square.color("white")
            new_square.penup()
            new_square.shapesize(2, 2)
            self.start[0] += -20
            new_square.goto(self.start[0], 0)
            self.segments.append(new_square)

    def move_up(self):
        self.segments[0].setheading(90)

    def move_down(self):
        self.segments[0].setheading(270)

    def move_left(self):
        self.segments[0].setheading(180)

    def move_right(self):
        self.segments[0].setheading(0)

    #self.initialize_snake()
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        self.segments[0].forward(10)

        #movements
        screen.onkeypress(key="Up", fun=self.move_up)
        screen.onkeypress(key="Down", fun=self.move_down)
        screen.onkeypress(key="Left", fun=self.move_left)
        screen.onkeypress(key="Right", fun=self.move_right)