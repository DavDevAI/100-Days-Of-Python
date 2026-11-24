from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.car_bank = []
        self.initialize_cars()

    def initialize_cars(self):
        for cars in range(len(COLORS)):
            new_car = Turtle(shape="square")
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.setheading(180)
            new_car.goto(random.randint(270, 300), random.randint(-250, 250))
            self.car_bank.append(new_car)

    def generate_traffic(self):
        new_car = Turtle(shape="square")
        new_car.penup()
        new_car.color(random.choice(COLORS))
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.setheading(180)
        new_car.goto(random.randint(299, 300), random.randint(-250, 250))
        self.car_bank.append(new_car)

    def move_cars(self):
        for car in self.car_bank:
            #if I want random pace movement for each and every car instead all of them moving at the same pace
            #car.forward(random.randint(0, STARTING_MOVE_DISTANCE+1))
            #THAT could give a more realistic touch if I wanted to make move each car at its own speed as happens in real life traffic
            #intead of everyone looking the same because they are moving at the same pace
            car.forward(STARTING_MOVE_DISTANCE)

            #define logic that if the current batch of cars passes the left bounday, remove them from the list to avoid memory overflow

            #define logic if every level is passed to increase the car speed by increasing the start moving distance
