from time import sleep
from turtle import Turtle

MOVING_DISTANCE = 25
SPEED = 0.2


class Snake:

    def __init__(self):
        self.snake_segments = []
        self.create_snake()

    def create_snake(self):
        for i in range(3):
            segment = Turtle()
            segment.shape("square")
            segment.color("White")
            segment.penup()
            segment.goto(i * -MOVING_DISTANCE, 0)
            segment.speed(1)
            self.snake_segments.append(segment)

    def move(self):
        for i in range(len(self.snake_segments) - 1, 0, -1):
            next_pos = self.snake_segments[i - 1].pos()
            self.snake_segments[i].goto(next_pos)
        self.snake_segments[0].forward(MOVING_DISTANCE)
        sleep(SPEED)
