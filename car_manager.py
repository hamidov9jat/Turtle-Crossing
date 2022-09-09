import random
from turtle import Turtle


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
NUMBER_OF_CARS = 15


class CarManager:
    def __init__(self):
        self._cars = []
        self._car_min_speed = STARTING_MOVE_DISTANCE
        self._car_max_speed = self._car_min_speed + MOVE_INCREMENT*3
        self.add_cars(number_of_cars=NUMBER_OF_CARS)

    def add_cars(self, number_of_cars: int):
        for car_colour_ in range(number_of_cars):
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
                new_y = random.randint(-250, 250)
                car_.goto(310, new_y)
            else:
                # car_.forward(STARTING_MOVE_DISTANCE)
                car_.backward(random.randrange(self._car_min_speed, self._car_max_speed))

    def level_up(self):
        self._car_min_speed += MOVE_INCREMENT
