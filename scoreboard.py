# Ali Jafarbeglou
from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scorboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-270, 260)
        self.update_scorboard()


    def update_scorboard(self):
        self.clear()
        self.write(f"Level: {self.level}", align= "left", font=FONT)


    def increase_level(self):
        self.level += 1
        self.update_scorboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align= "center", font=FONT)




