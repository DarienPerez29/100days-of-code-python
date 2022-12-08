import random
from turtle import Turtle, Screen

t = Turtle()
s = Screen()

s.colormode(255)


def get_rand_rgb():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


t.speed(0)

n_circles = 90
radius = 90
for _ in range(n_circles):
    t.color(get_rand_rgb())
    t.circle(radius)
    t.right(360/n_circles)

s.exitonclick()
