from turtle import Turtle

FONT = ("Courier", 20, "normal")


class SpeedoMeter(Turtle):
    def __init__(self, initial_speed: int):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(100, 250)
        self.update_speed(initial_speed)

    def update_speed(self, speed: int):
        self.clear()
        self.write(f"Speed: {speed}", font=FONT)
