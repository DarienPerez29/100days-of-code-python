from turtle import Turtle, Screen

t = Turtle()
s = Screen()
s.listen()


def clear():
    t.reset()


def move_forward():
    t.forward(10)


def move_backward():
    t.backward(10)


def turn_left():
    t.left(10)


def turn_right():
    t.right(10)


s.onkey(clear, "c")
s.onkeypress(move_forward, "w")
s.onkeypress(move_backward, "s")
s.onkeypress(turn_left, "a")
s.onkeypress(turn_right, "d")

s.exitonclick()
