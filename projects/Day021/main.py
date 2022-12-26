from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

# Comment from wsl
s = Screen()
s.setup(600, 600)
s.bgcolor("black")
s.title("Snake Game")
s.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

s.listen()
s.onkey(snake.up, "Up")
s.onkey(snake.down, "Down")
s.onkey(snake.left, "Left")
s.onkey(snake.right, "Right")

on_game = True
while on_game:
    s.update()
    snake.move()

    if snake.head.distance(food) < 12:
        food.new_pos()
        scoreboard.update_score()

s.exitonclick()
