from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color('black')
        self._level = 1
        self.goto(-290, 250)
        self.update_level()

    def update_level(self):
        self.clear()
        self.write(f"Level: {self._level}", font=FONT)

    def next_level(self):
        self._level += 1
        self.update_level()

    def game_over(self):
        self.home()
        self.write(f"Game Over!", align='center', font=FONT)

