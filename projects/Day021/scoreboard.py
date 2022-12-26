from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Consolas", 12, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(0, 270)
        self.hideturtle()
        self.color("white")
        self.score = -1
        self.update_score()

    def update_score(self):
        self.clear()
        self.score += 1
        self.write("Score: {}".format(self.score), False, ALIGNMENT, FONT)
