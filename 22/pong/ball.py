from turtle import Turtle

class Ball(Turtle):
    def __init__(self, paddle_left, paddle_right):
        super().__init__()
        # as I am inheriting from the Turtle I don't need and object and directly can pull Turtle's methods
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=.5, stretch_len=.5)  # stretching by .5 that means by its half, it was 20 by 20, now is 10 by 10
        self.color("white")
        self.speed("fastest")
        self.goto(0,0)
        self.dx = 10
        self.dy = -10
        self.left_pad = paddle_left
        self.right_pad = paddle_right
        self.bounce_physics()
        self.speed_res = 0.1

    def bounce_physics(self):
        #WHAT WE DO HERE IS SORT OF A COMPONENT X+Y movement each time the screen refreshes, we set movement in x axis and y axis at the same time a diagonal or component
        #movement is a composition of x and y vectors and inside the coodinates is a persisten sum of the current coodinates plus a delta (also differential in x) and the same
        #on y a differential or delta on y, doing it recursively each time the screen refreshes
        #print(f"current x value {self.dx}, current y value {self.dy}") used to debug the increment of dx and dy each reset if used
        self.setx(self.xcor() + self.dx)
        self.sety(self.ycor() + self.dy)

        #bouncing borders JUST TOP AND BOTTOM
        # Checking borders
        if self.ycor() > 280: # here is once I reach the upper wall limit
            self.sety(280) #set my self down before the bound
            self.dy *= -1  #do the shift in direction by chaning it to its negative "LIKE A ROTATIONAL" it rotates or inverses the movement the other way around, for this one i just shift
            # it to a negative value, the current delta value is having

        if self.ycor() < -280: #same for here but the other way around
            self.sety(-280)
            self.dy *= -1

        #COLLISIONS WITH THE PADDLE WHENEVER THE PADDLE TOUCHES THEM, previous implementation making the constraints of collision inside the if statement

        #detect collision with the right paddle
        if self.distance(self.right_pad) < 50 and self.xcor() > 305: #ITS 305 because the width of the paddle is 20 and I sent it to 325 so it is 325 - 20
            self.setx(305)
            self.dx *= -1
            self.speed_res *= 0.9
            print(f"speed incremented to: {self.speed_res}")

        #collision with left
        if self.distance(self.left_pad) < 50 and self.xcor() < -305:  # ITS 305 because the width of the paddle is 20 and I sent it to 325 so it is 325 - 20
            #inversed the greater than conditional logic because of the position of the xy plane and the shifting to negative numbers basic alg math
            self.setx(-305)
            self.dx *= -1
            self.speed_res *= 0.9
            print(f"speed incremented to: {self.speed_res}")


        #improved the bulky overcomplicated paddle collision
        # if (self.xcor() > 262 and self.xcor() < 270) and \
        #         (self.ycor() < self.right_pad.ycor() + 50 and self.ycor() > self.right_pad.ycor() - 50):
        #     self.setx(262)
        #     self.dx *= -1
        #
        # if (self.xcor() < -262 and self.xcor() > -270) and \
        #         (self.ycor() < self.left_pad.ycor() + 50 and self.ycor() > self.left_pad.ycor() - 50):
        #     self.setx(-262)
        #     self.dx *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.speed_res = 0.1

        #for debugging the increment on dx, dy resolution
        # self.dx += 5
        # self.dy = (self.dy) - (5)
        #
        # print(f"Speed resolution pace augmented to x: {self.dx}, y: {self.dy}")