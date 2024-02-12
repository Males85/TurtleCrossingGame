from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.speed = STARTING_MOVE_DISTANCE

    def add_car(self):
        car = Turtle("square")
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.color(random.choice(COLORS))
        car.penup()
        car.goto(300, random.randint(-250, 250))
        car.setheading(180)
        self.cars.append(car)

    def move_cars(self):
        for car in self.cars:
            car.forward(self.speed)

    def speed_up(self):
        self.speed += MOVE_INCREMENT

# class CarManager(Turtle):
#     def __init__(self):
#         super().__init__()
#         self.shape("square")
#         self.color(random.choice(COLORS))
#         self.penup()
#         self.goto(340, random.randint(-250, 250))
#         self.shapesize(stretch_wid=1, stretch_len=2)
#         self.setheading(180)
#         self.speed = STARTING_MOVE_DISTANCE
#
#     def move(self):
#         self.forward(self.speed)
#
#     def speed_increment(self):
#         self.speed += MOVE_INCREMENT





