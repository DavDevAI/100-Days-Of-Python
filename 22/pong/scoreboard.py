from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, "bold")

class Scoreboard(Turtle):
    def __init__(self, player_coords):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.startpos = player_coords
        self.goto(self.startpos)
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(self.score, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()