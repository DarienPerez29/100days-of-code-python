from turtle import Turtle, Screen

t = Turtle()
s = Screen()
s.listen()


def move_forwards():
    t.forward(10)


s.onkeypress(key="space", fun=move_forwards)
s.exitonclick()
