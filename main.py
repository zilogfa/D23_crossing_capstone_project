# Ali Jafarbeglou
# Crossing Capstone Projects
import random
from turtle import Turtle, Screen
from player import Player
import time
from car_manager import CarManager
from scoreboard import Scorboard


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("Crossing Game | Ali Jafarbeglou")
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scorboard()

screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    # collision with cars
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Detect successful crossing
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.car_level_up()
        scoreboard.increase_level()


screen.exitonclick()