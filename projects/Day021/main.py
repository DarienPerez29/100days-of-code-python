from snake import Snake
from turtle import Screen
from food import Food


s = Screen()
s.setup(600, 600)
s.bgcolor("black")
s.title("Snake Game")
s.tracer(0)

my_s = Snake()
my_f = Food()

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
