import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle crossing")
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()


screen.listen()
screen.onkey(player.move, 'Up')

game_is_on = True
new_cars = 0
cars = []
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.move_cars()

    new_cars += 1
    if new_cars == 6:
        car_manager.add_car()
        new_cars = 0

    # for car in cars:
    #     car.move()
    #
    if player.ycor() > 280:
        player.goto(0, -280)
        car_manager.speed_up()
        scoreboard.update_score()
        #print(car_manager.speed)
    for car in car_manager.cars:
        if player.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False






screen.exitonclick()