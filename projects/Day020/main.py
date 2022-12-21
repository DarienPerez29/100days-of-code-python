import snake
from turtle import Screen


s = Screen()
s.setup(600, 600)
s.bgcolor("black")
s.title("Snake Game")
s.tracer(0)

my_s = snake.Snake()
s.update()

on_game = True
while on_game:
    s.update()
    my_s.move()

s.exitonclick()
