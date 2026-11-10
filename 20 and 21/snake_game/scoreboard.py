from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 20, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        # I inherit from the turtle superclass
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 270)
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Food Score: {self.score}", True, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", True, align=ALIGNMENT, font=FONT)
    def increase_score(self):
        self.score += 1
        self.clear()
        self.goto(0, 270)
        self.update_scoreboard()
        #my approach hard coded
        # self.write(f"Food Score: {self.score}", True, align="Center", font=("Arial", 20, "bold"))
        # self.clear()
        # self.score += 1
        # self.goto(0, 250)
        # self.write(f"Food Score: {self.score -1 }", True, align=ALIGMENT, font=FONT)


