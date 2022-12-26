import random
from turtle import Turtle


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color("cyan")
        self.speed(0)
        self.new_pos()

    def new_pos(self):
        rx = random.randint(-11, 11) * 25
        ry = random.randint(-11, 11) * 25
        self.goto(rx, ry)
