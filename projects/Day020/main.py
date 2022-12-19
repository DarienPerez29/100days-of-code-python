from turtle import Turtle, Screen

s = Screen()
s.setup(600, 600)
s.bgcolor("black")
s.title("Snake Game")
snake_segments = []

for _ in range(3):
    segment = Turtle()
    segment.shape("square")
    segment.color("White")
    snake_segments.append(segment)

for i, segment in enumerate(snake_segments):
    segment.goto(i * -20, 0)

s.exitonclick()
