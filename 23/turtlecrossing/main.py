import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
cars = CarManager()
score = Scoreboard()

screen.onkeypress(key="Up", fun=player.move_up)

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    cars.generate_cars()
    cars.move_cars()