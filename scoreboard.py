from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.level = 1
        self.goto(x=-280, y=250)
        self.show_level()

    def show_level(self):
        self.clear()
        self.write(f"Level {self.level}", align="center", font=FONT)

    def game_over(self):
        self.home()
        self.write("Game Over", align="center", font=FONT)

    def increase_level(self):
        self.level += 1
        self.show_level()
