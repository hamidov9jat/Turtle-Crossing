import random
from turtle import Turtle


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
NUMBER_OF_CARS = 15


class CarManager:
    def __init__(self):
        self._cars = []
        self._car_speed = STARTING_MOVE_DISTANCE
        # self._car_max_speed = self._car_min_speed + MOVE_INCREMENT*3

    def add_cars(self):

        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle('square')
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_y = random.randint(-250, 250)
            new_car.goto(310, new_y)
            # new_car.setheading(180)
            self._cars.append(new_car)

    def move_cars(self):
        for car_ in self._cars:
            if car_.xcor() < -310:
                self._cars.remove(car_)
            else:
                # car_.forward(STARTING_MOVE_DISTANCE)
                car_.backward(self._car_speed)

    def level_up(self):
        self._car_speed += MOVE_INCREMENT
