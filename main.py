from turtle import Screen
from myturtle import Myturtle
from Scoreboard import Scoreboard
from cars import Mycar

import random
import time
screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("white")
screen.title("Turtle Road Cross")
screen.tracer(0)

screen.listen()
car = Mycar()
turtle1 = Myturtle((0,-250))
level = int(input("Select Difficulty level, 1: Beginner, 2:Intemediate, 3: Adavance:  "))
pace = level * 2
score = Scoreboard(level)
screen.onkey(turtle1.up,"Up")
screen.onkey(turtle1.down,"Down")
screen.onkey(turtle1.left,"Left")
screen.onkey(turtle1.right,"Right")
game_continues = True
while game_continues:
    screen.update()
    time.sleep(0.01)
    car.create_car()
    car.car_move(pace)
    # if car.collision_detect(turtle1):
        # game_continues = False
    for cars in car.all_cars:
        if cars.distance(turtle1)< 20:
            score.game_over()
            game_continues = False

    if turtle1.ycor() > 290:
        print("You win")
        pace += 1
        turtle1.reset((0,-250))
        score.add_points()

screen.exitonclick()


