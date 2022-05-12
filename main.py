from turtle import Screen
from myturtle import Myturtle
from cars import Mycar
car_position = [(280,280),(280,240),(280,200),(280,160),(280,120),(280,80),(280,40),(280,-280),(280,-240),(280,-200),(280,-160),(280,-120),(280,-80),(280,-40),(280,0)]
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

# level = int(input("Select Difficulty level, 1: Beginner, 2:Intemediate, 3: Adavance:  "))
# pace = level * 2
pace = 1
screen.onkey(turtle1.up,"Up")

game_continues = True
while game_continues:
    screen.update()
    time.sleep(0.01)
    car.create_car()
    car.car_move(pace)

    if car.distance(turtle1) < 20:
        car.collision_detect()
        game_continues = False

    # Detect collision with wall.
    if car.xcor() < -380:
        print("car hit -380")
        car.car_reset()

    if turtle1.ycor() > 290:
        print("You win")
        game_continues = False
screen.exitonclick()


