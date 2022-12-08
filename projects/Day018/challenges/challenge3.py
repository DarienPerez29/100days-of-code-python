import random
from turtle import Turtle, Screen

t = Turtle()
s = Screen()

s.colormode(255)

for i in range(3, 11):
    deg = ((i - 2) * 180) // i

    r_rand = int(random.randrange(0, 255))
    g_rand = int(random.randrange(0, 255))
    b_rand = int(random.randrange(0, 255))
    t.color(r_rand, g_rand, b_rand)

    for j in range(i):
        t.forward(50)
        t.right(180 - deg)

s.exitonclick()
