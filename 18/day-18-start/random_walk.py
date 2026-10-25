from turtle import Turtle, Screen
import random


screen = Screen()
line = Turtle()

directions = [0, 90, 180, 270]
#in other coordinate notation [0,0] = 0 grades, [0,1] = 90 grades, [-1,0] = 180 grades, [0,-1] = 270 grades, [1,0] = 360 grades, [1,1] = 45 grades
thickness = 0
for _ in range(1000): # set it 1000 times to draw
    line.color(random.choice(["red", "green", "blue", "CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat","SlateGray", "SeaGreen"]))
    line.forward(10)
    line.setheading(random.choice(directions))
    thickness += 0.1
    line.pensize(thickness)
