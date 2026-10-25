#use turtle but now as a MODULE AND NOT A CLASS
import turtle as t
import random

tim = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b  #REMEMBER ALWAYS RETURN AS A TUPLE STARTING WITH 2 OR MORE VARIABLES


directions = [0, 90, 180, 270]
#in other coordinate notation [0,0] = 0 grades, [0,1] = 90 grades, [-1,0] = 180 grades, [0,-1] = 270 grades, [1,0] = 360 grades, [1,1] = 45 grades
thickness = 0
tim.speed("fastest")
for _ in range(1000): # set it 1000 times to draw
    tim.color(random_color())
    tim.forward(10)
    tim.setheading(random.choice(directions))
    thickness += 0.1
    tim.pensize(thickness)
