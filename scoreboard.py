from turtle import Turtle

FONT = ("Courier", 24, "normal")
SCOREBOARD_COORDINATES = (-220, 260)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("black")
        self.hideturtle()
        self.penup()
        self.goto(SCOREBOARD_COORDINATES)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Level: {self.level}", align="center", font=FONT)
        self.level += 1

    def game_over(self):
        self.home()
        self.write("GAME OVER", align='center', font=FONT)
