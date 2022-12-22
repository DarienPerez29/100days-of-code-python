import snake
from turtle import Screen


s = Screen()
s.setup(600, 600)
s.bgcolor("black")
s.title("Snake Game")
s.tracer(0)

my_s = snake.Snake()
s.listen()
s.onkey(my_s.up, "Up")
s.onkey(my_s.down, "Down")
s.onkey(my_s.left, "Left")
s.onkey(my_s.right, "Right")

on_game = True
while on_game:
    s.update()
    my_s.move()

s.exitonclick()
