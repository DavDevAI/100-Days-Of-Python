from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        # I inherit from the turtle superclass
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 250)
        self.score = 0
        self.write(f"Food Score: {self.score}", True, align="Center", font=("Arial", 20, "bold"))

        self.increase_score()

    def increase_score(self):
        self.score += 1


