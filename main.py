import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

turtle_player = Player('turtle')
level_board = Scoreboard()
carmanager = CarManager()

screen.listen()
screen.onkeypress(fun=turtle_player.move_up, key='Up')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    carmanager.add_cars()
    carmanager.move_cars()

    # Detect collision with car
    for car_ in carmanager._cars:
        if car_.distance(turtle_player) < 20:
            game_is_on = False
            level_board.game_over()

    # Detect successful crossing
    if turtle_player.is_at_finish_line():
        turtle_player.go_to_start()
        carmanager.level_up()
        level_board.next_level()

screen.exitonclick()
