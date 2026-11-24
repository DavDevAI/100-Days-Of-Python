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
cars = CarManager(player ) #i pass here the fixed object that never changes
score = Scoreboard()

screen.onkeypress(key="Up", fun=player.move_up)

game_is_on = True

count = 0
while game_is_on:
    time.sleep(0.1)
    screen.update()
    count += 1

    cars.move_cars()

    if count % 6 == 0:
        print(f"refresh at {count}")
        cars.generate_traffic() #until here its good, but also to make it even more random, each 6 refreshes form a list and pick in which time of those six I generate

    if player.ycor() > 296:
        #increase level, by scoring a level upgrade and increasing traffic speed
        score.increase_score()
        player.reset_position()
        cars.increase_speed(cars.move_cars())


    if not cars.check_collision():
        game_is_on = False
        score.game_over()