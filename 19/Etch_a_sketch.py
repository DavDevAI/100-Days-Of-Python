from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

# EVENT LISTENERS, FOR PYTHON AND SPECIFIC FOR THIS LIBRARY AN EVENT LISTENER IS BASICALLY LIKE AN INTERRUPTION EVENT AS OTHER LANGUAGES (C, ASSY)

def move_forward():
    tim.forward(10)
def move_backward():
    tim.backward(10)
def ccw():
    tim.left(10)
def cw():
    tim.right(10)
def clear():
    tim.reset()



screen.listen()
screen.onkeypress(key = "w", fun = move_forward)
screen.onkeypress(key = "s", fun = move_backward)
screen.onkeypress(key = "a", fun = ccw)
screen.onkeypress(key = "d", fun = cw)
screen.onkeypress(key = "c", fun = clear)

screen.exitonclick()
