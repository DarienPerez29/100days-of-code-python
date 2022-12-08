from turtle import Turtle, Screen

my_turtle = Turtle()

line_dash_size = 10
for _ in range(10):
    my_turtle.pendown()
    my_turtle.forward(line_dash_size)
    my_turtle.penup()
    my_turtle.forward(line_dash_size)

my_screen = Screen()
my_screen.exitonclick()
