import random
from turtle import Turtle


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self._cars = []
        self._car_speed = STARTING_MOVE_DISTANCE
        self.add_cars(10)

    def add_cars(self, number_of_cars: int):
        for car_colour_ in range(number_of_cars):
            new_car = Turtle('square')
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.goto(310, random.randint(-280, 280))
            # new_car.setheading(180)
            self._cars.append(new_car)

    def move_cars(self):
        for car_ in self._cars:
            if car_.xcor() < -310:
                car_.goto(310, random.randint(-280, 280))
            else:
                # car_.forward(STARTING_MOVE_DISTANCE)
                car_.backward(STARTING_MOVE_DISTANCE)

    def level_up(self):
        self._car_speed += MOVE_INCREMENT
