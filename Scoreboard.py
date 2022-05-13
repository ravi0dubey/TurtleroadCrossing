from turtle import Turtle
INCR = 1
FONT = ('Courier', 15, "bold")
ALIGNMENT = 'center'

class Scoreboard(Turtle):
    def __init__(self,level):
        super().__init__()
        self.points1 = 0
        self.level= level
        self.score = 0
        self.penup()
        self.ht()
        self.color("black")
        self.score_write()

    def score_write(self):
        self.clear()
        self.goto(-250,260)
        self.write(f"Level {self.level} Score:{self.score}", align=ALIGNMENT, font=FONT)

    def add_points(self):
        self.score += INCR
        self.score_write()
    def game_over(self):
        self.goto(-50, 0)
        self.write("Game Over", align=ALIGNMENT, font=FONT)
