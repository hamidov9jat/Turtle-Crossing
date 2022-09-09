from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
INCREMENT_SPEED = 10
MAX_SPEED = 50


class Player(Turtle):
    def __init__(self, shape: str):
        super().__init__(shape)
        self.penup()
        self.setheading(90)
        self.go_to_start()
        self._turtle_speed = MOVE_DISTANCE

    def move_up(self):
        self.forward(self._turtle_speed)

    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self):
        return int(self.ycor()) > FINISH_LINE_Y

    def increase_speed(self):
        if self._turtle_speed < MAX_SPEED:
            self._turtle_speed += INCREMENT_SPEED

    def decrease_speed(self):
        if self._turtle_speed > MOVE_DISTANCE:
            self._turtle_speed -= INCREMENT_SPEED
