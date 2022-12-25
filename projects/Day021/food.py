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
        rx = random.randint(-280, 280)
        ry = random.randint(-280, 280)
        self.goto(rx, ry)
