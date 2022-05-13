from turtle import Turtle
INCR = 1
FONT = ('Courier', 30, "bold")
ALIGNMENT = 'center'

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.points1 = 0
        self.score = 0
        self.penup()
        self.ht()
        self.color("black")
        self.score_write()

    def score_write(self):
        self.clear()
        self.goto(-40,260)
        self.write(f"Score : {self.score}", align=ALIGNMENT, font=FONT)


    def add_points(self):
        self.score += INCR
        self.score_write()

