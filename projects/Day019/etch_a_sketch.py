from turtle import Turtle, Screen

t = Turtle()
pen_down = True
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


def alter_pen():
    global pen_down
    if pen_down:
        t.penup()
        pen_down = False
    else:
        t.pendown()
        pen_down = True


s.onkey(clear, "c")
s.onkeypress(move_forward, "w")
s.onkeypress(move_backward, "s")
s.onkeypress(turn_left, "a")
s.onkeypress(turn_right, "d")
s.onkeypress(alter_pen, "p")

s.exitonclick()
