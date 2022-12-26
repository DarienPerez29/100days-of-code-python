from time import sleep
from turtle import Turtle

MOVING_DISTANCE = 20
SPEED = 0.1


class Snake:
    def __init__(self):
        # Create serpent
        self.snake_segments = []
        self.create_snake()
        self.head = self.snake_segments[0]
        self.heading = self.head.heading()

    def create_snake(self):
        # Create serpent segments
        for i in range(3):
            segment = Turtle()
            segment.shape("square")
            segment.color("White")
            segment.penup()
            segment.goto(i * -MOVING_DISTANCE, 0)
            segment.speed(1)
            self.snake_segments.append(segment)

    def move(self):
        # Move serpent
        for i in range(len(self.snake_segments) - 1, 0, -1):
            next_pos = self.snake_segments[i - 1].pos()
            self.snake_segments[i].goto(next_pos)
        self.head.forward(MOVING_DISTANCE)
        self.heading = self.head.heading()
        sleep(SPEED)

    def up(self):
        # Turn up snake
        if self.heading == 0 or self.heading == 180:
            self.head.setheading(90)

    def down(self):
        # Turn down snake
        if self.heading == 0 or self.heading == 180:
            self.head.setheading(270)

    def left(self):
        # Turn left snake
        if self.heading == 90 or self.heading == 270:
            self.head.setheading(180)

    def right(self):
        # Turn right snake
        if self.heading == 90 or self.heading == 270:
            self.head.setheading(0)
