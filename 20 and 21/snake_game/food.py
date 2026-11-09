from turtle import Turtle

#Turtle is our superclass
class Food(Turtle): #we want to inherit food from the turtle class instead of creating the object for food in the initializer or constructor
    def __init__(self):
        super().__init__()
        #as I am inheriting from the Turtle I don't need and object and directly can pull Turtle's methods
        self.shape("circle")
