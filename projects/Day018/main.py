import colorgram
import random
from turtle import Turtle, Screen

t = Turtle()
s = Screen()
t.penup()
t.hideturtle()
t.speed(0)
t.shape("circle")
t.color("gray")
s.colormode(255)

my_colors = []
colors = colorgram.extract('projects/Day018/image.jpg', 50)
PAINT_SIZE = 20
DOT_DIAMETER = 10
DOT_SPACING = 30


def align_turtle():
    t.backward(DOT_SPACING * PAINT_SIZE // 2)
    t.right(90)
    t.forward(DOT_SPACING * PAINT_SIZE // 2)
    t.left(90)


for color in colors:
    color_rgb = tuple(color.rgb)
    rc = color_rgb[0]
    gc = color_rgb[1]
    bc = color_rgb[2]

    if color_rgb not in my_colors:
        if ((rc < 200 or gc < 200 or bc < 200)
                and (rc > 100 or gc > 100 or bc > 100)):
            my_colors.append(color_rgb)

align_turtle()
for y in range(PAINT_SIZE):
    for x in range(PAINT_SIZE):
        t.dot(DOT_DIAMETER, random.choice(my_colors))
        t.forward(DOT_SPACING)
    t.backward(DOT_SPACING * PAINT_SIZE)
    t.left(90)
    t.forward(DOT_SPACING)
    t.right(90)

s.exitonclick()
