from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Myturtle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.setheading(UP)
        self.goto(position)

    def up(self):
        new_y = self.ycor()+MOVE_DISTANCE
        self.goto(self.xcor(),new_y)

    def down(self):
        new_y = self.ycor()- MOVE_DISTANCE
        self.goto(self.xcor(),new_y)

    def left(self):
        new_x= self.xcor()- MOVE_DISTANCE
        self.goto(new_x,self.ycor())

    def right(self):
        new_x= self.xcor()+ MOVE_DISTANCE
        self.goto(new_x,self.ycor())

    def reset(self,position):
        self.goto(position)