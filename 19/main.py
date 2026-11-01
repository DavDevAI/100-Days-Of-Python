from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

# EVENT LISTENERS, FOR PYTHON AND SPECIFIC FOR THIS LIBRARY AN EVENT LISTENER IS BASICALLY LIKE AN INTERRUPTION EVENT AS OTHER LANGUAGES (C, ASSY)

def move_forward():
    tim.forward(100)


screen.listen() #recursively listening or actively running a parallel process that listens to an interruption
#FUNCTIONS AS AN INPUT, USING move_forward() as a paramater for another function
screen.onkey(key = "space", fun = move_forward) #because is actively listening (like a forever while loop on a microcontroller or a always executing thing on web app or server)
#It will walk whenever I press space like a game that is always playing and waiting for our commands
#or like a robotics arm or project that is always listening and awating and reacting for any given command
screen.exitonclick()
