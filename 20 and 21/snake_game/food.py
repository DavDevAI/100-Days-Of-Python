from turtle import Turtle
import random
#Turtle is our superclass
class Food(Turtle): #we want to inherit food from the turtle class instead of creating the object for food in the initializer or constructor
    def __init__(self):
        super().__init__()
        #as I am inheriting from the Turtle I don't need and object and directly can pull Turtle's methods
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=.5, stretch_len=.5) #stretching by .5 that means by its half, it was 20 by 20, now is 10 by 10
        self.color("yellow")
        self.speed("fastest")
        self.refresh_food()

    def refresh_food(self):
        self.goto(random.randint(-270, 270), random.randint(-270, 270))
