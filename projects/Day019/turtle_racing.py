from turtle import Turtle, Screen

s = Screen()

S_WIDTH = 750
S_HEIGHT = 500
s.setup(S_WIDTH, S_HEIGHT)
colors = ["red", "green", "blue", "orange", "purple", "brown"]
turtles = []

for i, color in enumerate(colors):
    turtles.append(Turtle())
    turtles[i].shape("turtle")
    turtles[i].color(color)
    turtles[i].penup()

pos = 120
for turtle in turtles:
    turtle.setpos(-7 * (S_HEIGHT // 10), pos)
    pos -= 40


s.exitonclick()
