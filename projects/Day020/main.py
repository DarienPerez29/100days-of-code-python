from time import sleep
from turtle import Turtle, Screen

SPEED = 0.1

s = Screen()
s.setup(600, 600)
s.bgcolor("black")
s.title("Snake Game")
s.tracer(0)
snake_segments = []

# Creating segments
for i in range(3):
    segment = Turtle()
    segment.shape("square")
    segment.color("White")
    segment.penup()
    segment.goto(i * -20, 0)
    segment.speed(1)
    snake_segments.append(segment)

on_game = True
while on_game:
    s.update()
    sleep(SPEED)
    for i in range(len(snake_segments) - 1, 0, -1):
        next_pos = snake_segments[i - 1].pos()
        snake_segments[i].goto(next_pos)
    snake_segments[0].forward(20)
    snake_segments[0].left(90)


s.exitonclick()
