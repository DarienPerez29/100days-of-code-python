import random
from turtle import Turtle, Screen
from tkinter import messagebox

# Setup screen
s = Screen()
s.title("Turtle Racing")
S_WIDTH = 750
S_HEIGHT = 500
s.setup(S_WIDTH, S_HEIGHT)
FINISH_POINT = 7 * S_HEIGHT // 10
START_POINT = -1 * FINISH_POINT

# Initialize game
on_race = False
colors = ["red", "green", "blue", "orange", "purple", "brown"]
turtles = []

for i, color in enumerate(colors):
    turtles.append(Turtle())
    turtles[i].shape("turtle")
    turtles[i].color(color)
    turtles[i].penup()

pos = 120
for turtle in turtles:
    turtle.setpos(START_POINT, pos)
    pos -= 40

# Ask for bet color
while True:
    user_bet = s.textinput(
        "Make your bet",
        "Which turtle you think will win the race? \nEnter a color: "
    ).lower()

    if user_bet in colors:
        on_race = True
        break
    else:
        messagebox.showinfo(
            "Invalid color",
            "Please enter one of these colors: {}.".format(", ".join(colors))
        )

winner = ""
while on_race:
    for i, turtle in enumerate(turtles):
        turtle.forward(random.randint(0, 10))

        if turtle.xcor() >= FINISH_POINT:
            on_race = False
            winner = turtle.pencolor()


if winner == user_bet:
    messagebox.showinfo(
        "You've won!",
        "The {} turtle has won the race. Congrats!!!".format(winner)
    )
else:
    messagebox.showinfo(
        "You've lost...",
        "The {} turtle has won the race. Luck for the next.".format(winner)
    )
