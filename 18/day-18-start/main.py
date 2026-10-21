from turtle import Turtle, Screen
import random
#import heroes

timmy = Turtle()
timmy.shape("turtle")
timmy.color("red")
# print (heroes.gen())
#
# for _ in range(4): # as I thought its always USING my underscore if I DON'T WANT AN ITERATOR VARIABLE IN THE LOOP
#     timmy.forward(100)
#     timmy.right(90)

#drawing a doted line logic
# for i in range(100):
#     timmy.forward(5)
#     if i % 2 == 0:
#         timmy.penup()
#     else:
#         timmy.pendown()

# def triangle ():
#     for _ in range (3):
#         timmy.forward(100)
#         timmy.left(120)
#         timmy.forward(100)
#     timmy.home()  # we can send him also to coordinates
# def square ():
#     for _ in range (4):
#         timmy.forward(100)
#         timmy.left(90)
#
#     timmy.home()  # we can send him also to coordinates
# def pentagon ():
#     for _ in range(5):
#         timmy.forward(100)
#         timmy.left(72)
#     timmy.home()  # we can send him also to coordinates
# def hexagon ():
#     for _ in range(6):
#         timmy.forward(100)
#         timmy.left(60)
#     timmy.home()
# def heptagon ():
#     for _ in range(7):
#         timmy.forward(100)
#         timmy.left(51.428)
#     timmy.home()
# def octagon ():
#     for _ in range(8):
#         timmy.forward(100)
#         timmy.left(45)
#     timmy.home()
# def nonagon ():
#     for _ in range(9):
#         timmy.forward(100)
#         timmy.left(40)
#     timmy.home()
# def decagon ():
#     for _ in range(9):
#         timmy.forward(100)
#         timmy.left(36)
#     timmy.home()

figures = 0
num_sides = 2
while figures <= 7:
    num_sides += 1
    timmy.color(random.choice(["red", "green", "blue", "CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]))
    for _ in range(num_sides):
        angle = 360 / num_sides
        timmy.forward(100)
        timmy.left(angle)
    figures += 1

screen = Screen()
screen.exitonclick()