import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


# 1. Creating a player and moving upward.
player = Player()
# 2. Create and move the cars.
car_Manager = CarManager()

# 1. Creating a player and moving upward.
screen.listen()
screen.onkey(player.go_up, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # 2. Create and move the cars.
    car_Manager.create_car()
    car_Manager.move_cars()

    # 3. Detect collision with cars
    for car in car_Manager.all_cars:
        if car.distance(player) < 25 :
            game_is_on = False
    
    # 4. Detect a successful crossing.
    if player.is_at_finish_line():
        player.go_to_start()
        car_Manager.level_up()


screen.exitonclick()

