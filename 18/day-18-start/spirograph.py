import turtle as t
import random

tim = t.Turtle()
t.colormode(255)



def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b

#tim.speed("fastest")

def draw_spirograph(resolution):
    for _ in range(int(360/resolution)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + resolution)

    #my code for but with inverse logic
    # for _in in range(times_to_divide = 100) #times I want to fit inside 360 or to divide into 360
    #     tim.color(random_color())
    #     tim.circle(100)
    #     tim.left(360/times_to_divide)

draw_spirograph(10)




