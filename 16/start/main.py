#import anothermodule
#print(anothermodule.anothervar)
#import turtle
#timmy = turtle.Turtle() # se puede construir de esta manera la clase y guardarla en este objeto llamado Timmy"
import turtle
#BEST WAY TO DO IT
from turtle import Turtle, Screen

#TEST LEARNING ON HOW TO CREATE OBJECTS FROM CLASSES, SPECIFICALLY FROM EXISTING PYTHON MODULES OR LIBRARIES
#IN THIS CASE THE BASIC GUI GRAPHIC LIBRARY TURTLE
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("red")
# #timmy.speed(50)
# timmy.forward(100)
# my_screen = Screen() # method for creating the static screen
#
# print(my_screen.canvheight)
# my_screen.exitonclick() #this method will close when the click event happens so it keeps waiting so when it is clicked it will close, bc that is the method for closing

from prettytable import PrettyTable

table = PrettyTable()
print (table)
