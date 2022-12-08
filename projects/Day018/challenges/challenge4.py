import random as r
from turtle import Turtle, Screen

t = Turtle()
s = Screen()

t.pensize(10)
t.speed(0)
s.colormode(255)

deg_list = (0, 90, 180, 270)

for _ in range(200):
    rc = r.randrange(0, 255)
    gc = r.randrange(0, 255)
    bc = r.randrange(0, 255)
    t.color(rc, gc, bc)

    t.forward(20)
    deg = r.choice(deg_list)
    t.right(deg)

s.exitonclick()
