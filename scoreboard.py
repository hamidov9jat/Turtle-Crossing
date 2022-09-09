from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color('black')
        self._level = 1
        self.update_level()

    def update_level(self):
        self.clear()
        self.goto(-290, 250)
        self.write(f"Level: {self._level}", font=FONT)

    def next_level(self):
        self._level += 1
        self.update_level()

