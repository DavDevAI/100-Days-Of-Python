from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width = 800, height = 600) # WHEN IS A LIBRARY THING AND DOESNT KNOW EXACTLY WHAT MEANS EACH MARAMETERS WE USE THE EXPLICIT PARAMETER like width = 600
screen.bgcolor("black") #changing background color and name it as black I want it black
screen.title("David´s Snake Game")
screen.tracer(0)
screen.listen()

start = [0,0]
segments = []
for _ in range(3):
    new_square = Turtle(shape="square")
    new_square.color("white")
    new_square.penup()
    new_square.shapesize(2,2)
    start[0] += -20
    new_square.goto(start[0],0)
    segments.append(new_square)

def move_up():
    segments[0].setheading(90)
def move_down():
    segments[0].setheading(270)
def move_left():
    segments[0].setheading(180)
def move_right():
    segments[0].setheading(0)


game_is_on = True

while game_is_on:
    screen.update() #Here I make that each time ALL of the segments move I update all of them after they finish to make them look move as a whole
    time.sleep(0.1) #adds 0.1 second of delay after ALL of the segments move and are updated
    #LEGACY FOR LOOP USED STILL CAN BE USED IF I CAN REVERSE THE LIST PREVIOUSLY OR EACH TIME IS UPDATED
    #using segments.reverse() and creating sort of a new list
    # for segment in segments:
    #     segment.forward(10)
    # screen.update()
    # time.sleep(0.1) # adds 1 second of delay after each segments updates and moves
    for seg_num in range(len(segments)-1, 0, -1):  #(start = 2, stop = 0, range= -1) this one tells us that that we start from the end, want to stop at the begining and the negative range tells us that we are going backwards or decending

        new_x = segments[seg_num-1].xcor() #MY ITERATOR THAT NOW IS PASSING THRU THE LAST ELEMENT OF THE LIST BECAUSE ITS STARTING FROM THE END
        #now I assign it as an x coordinate because I am getting the x coordinate of the last
        #the "seg_num -1" determines that is not the LAST but the SECOND LAST which is the previous I have, that means THE ONE IN FRONT OF ME SO THE LAST ONE
        #GOES where the one in front of him was and the subsequent goes to where the one infront of him was, an so on and so forth
        new_y = segments[seg_num-1].ycor()
        segments[seg_num].goto(new_x,new_y)

    #NOW I push forward all the way from the back
    segments[0].forward(10)
    #now that the 'from the last one mechanic' is implemented i don't need to push from the foor loop
    #i forever push outside from the for loop, by staying in the while loop because i forever update the position of the last one by always pushing forward the last one by always pushing in the
    #while loop

    #MOVEMENTS
    screen.onkeypress(key="Up", fun=move_up)
    screen.onkeypress(key="Down", fun=move_down)
    screen.onkeypress(key="Left", fun=move_left)
    screen.onkeypress(key="Right", fun=move_right)


screen.exitonclick()

# TODO 1 HOW DO I MOVE IT ?
#TAKE INTO ACCOUNT THE MECHANICS FROM ETCH A SKETCH for moving with keay presses
# for the continous movements, take into account the forever movement for the turlte race

#TODO 2 HOW DO WE LINK EACH SEGMENT OF THE SNAKE?
#Take into account by using the all the way arround method, ,aking the last segment of the snake to mve where the subsecuent one was before all the way up to the first segment
#how can i do that? by reversing the list using the .reverse() method

#TODO 3 HOW THE APPENDING AND CHASING MECHANICS
#RANDOM CHOICE FROM A POOL OF COORDINATES FOR THE #FOOD TO BE TAKEN, APPENDING AND GENERATING A NEW OBJECT EACH TIME THE SNAKE EATS SOMETHING