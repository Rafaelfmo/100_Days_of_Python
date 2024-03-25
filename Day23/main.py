from turtle import Screen
from animal import Animal
from cars import Car
from score import Score
import time

# Screen configs
screen = Screen()
screen.bgcolor("Black")
screen.title("Animal Crossing")
screen.setup(600, 600)
screen.tracer(0)
screen.listen()


# Create objects
animal = Animal()
cars = Car()
score = Score()

# Config keys
screen.onkey(animal.move_up, "Up")
screen.onkey(animal.move_down, "Down")
screen.onkey(animal.move_left, "Left")
screen.onkey(animal.move_right, "Right")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    cars.create_car()
    cars.move_cars()

    for car in cars.all_cars:
        if car.distance(animal) < 20:
            score.game_over()
            game_is_on = False

    if animal.ycor() > 280:
        score.update_score()
        animal.level_up()


screen.exitonclick()