from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self, shape: str):
        super().__init__(shape)
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def move(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.sety(new_y)

    def is_finished(self):
        return int(self.ycor()) == FINISH_LINE_Y

