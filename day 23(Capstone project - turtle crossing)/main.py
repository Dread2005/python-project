import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard_turtle_ import Scoreboard

carss = []

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move_up, key="w")
screen.onkey(player.move_down, key="s")
screen.onkey(player.move_right, key="d")
screen.onkey(player.move_left, key="a")

cars = CarManager()

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create()
    time.sleep(0.3)
    cars.car_move()

    for the_cars in cars.all_cars:
        if the_cars.distance(player) < 10:
            game_is_on = False
            scoreboard.game_over()

        if player.is_player_there():
            player.reset_()
            cars.speed_up()
            scoreboard.next_level()






screen.exitonclick()
