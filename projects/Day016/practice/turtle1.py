import turtle
import turtle1_module

# print(turtle1_module.a_variable)

timmy = turtle.Turtle()
my_screen = turtle.Screen()

timmy.shape("turtle")
timmy.shapesize(1, 1, 2)
timmy.color("DarkOliveGreen", "DarkOliveGreen3")

timmy.forward(100)

my_screen.exitonclick()
