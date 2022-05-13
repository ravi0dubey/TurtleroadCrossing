import turtle
from turtle import Turtle
import random

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
car_color =["pink","red","yellow","cyan","magenta","blue"]
car_position = [(280,280),(280,240),(280,200),(280,160),(280,120),(280,80),(280,40),(280,0),(280,-40),(280,-80),(280,-120),(280,-160),(280,-200),(280,-240),(280,-280)]

class Mycar(Turtle):
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.ht()


    def create_car(self):
        random_chance = random.randint(1,20)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.penup()
            new_car.color(random.choice(car_color))
            new_car.setheading(LEFT)
            new_y = random.randint(-250,250)
            new_car.goto(300,new_y)
            self.all_cars.append(new_car)

    def car_move(self,pace):
        for car in self.all_cars:
            new_x = car.xcor() - pace
            car.goto(new_x,car.ycor())

    def collision_detect(self, turtle1):
        for car in self.all_cars:
            if car.distance(turtle1) < 20:
                print("Game Over")
                return True

    # def car_reset(self):
    #     self.goto(300,0)