# import colorgram as c
import random
import turtle as t

tim = t.Turtle()
screen = t.Screen()
t.colormode(255)
screen.screensize(600, 600) #HEIGHT OF CANVAS SCROLLING SPACE NOT JUST PIXELS
#screen.setup(600, 600)  #I USE THIS IF I WANNA SET THE SCREEN SIZE BY PIXEL SIZE IN THE WHOLE CANVAS AND NOT SCROLLING SIZE
# pallette = c.extract('image.jpg', 30)
#
# rgb_pallet = []
# for colors in pallette:
#     rgb = colors.rgb #here I can cast once it converts and already assign to rgb to make it already a tuple data type rgb = tuple(colors.rgb)
#     #hago esto porque el metodo .rgb() de la libreria me devuelve en RGB pero del tipo 'namedtuple', que en terminos practicos es un objeto y casteo para que sea
#     #una simple tupla
#     rgb_pallet.append(tuple(rgb))
# print(rgb_pallet)

color_pallette = [(199, 175, 117), (125, 36, 24), (187, 158, 51), (170, 104, 56), (5, 57, 83), (222, 223, 226), (200, 216, 204), (108, 67, 85), (39, 36, 35), (86, 142, 59), (20, 122, 176), (110, 161, 175), (75, 39, 47), (9, 67, 47), (64, 153, 137), (133, 41, 43), (184, 98, 80), (179, 201, 186), (209, 200, 115), (179, 174, 177), (151, 176, 165), (93, 142, 156), (28, 80, 59), (194, 190, 192), (17, 78, 99), (212, 184, 174), (142, 117, 123), (175, 198, 204)]



def dot_painting(x_dot,y_dot):
    tim.penup()
    tim.hideturtle()
    start = [-225, -225]
    tim.goto(start)
    for y in range(y_dot):
        for x in range(x_dot):
            tim.goto(start[0] + x*50, start[1] + y*50)  # To make it more dynamical it goes accumulating each iteration that's why y define y and x in the for loops
            tim.dot(20, random.choice(color_pallette))
            #tim.forward(50)
        #start[1] += 50
        #tim.goto(start[0], start[1])

dot_painting (10, 10)

screen.exitonclick()