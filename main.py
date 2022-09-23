import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    screen.listen()
    screen.onkey(fun=player.move, key="Up")

    # Player reaches finish line
    if player.finish():
        player.next_level()
        scoreboard.increase_level()

    # Detect collision with car
    for car in car_manager.all_cars:
        if player.distance(car.position()) < 20:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
