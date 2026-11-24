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
        #self.car_bank = car_bank

    def move_up(self):
        self.sety(self.ycor() + MOVE_DISTANCE)

    def check_collision(self):
        pass
        # for car in self.car_bank:
        #     if self.distance(car) < 50:
        #         return False

    def reset_position(self):
        self.goto(0, -270)
