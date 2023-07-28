import turtle as t
import random
from random import choice
from turtle import Screen

randomTurtle = t.Turtle()
t.colormode(255)


def random_color():
    """Returns random rgb values for the pencolor."""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


# different movements
moves = ["forward", "left", "right", "backward"]
# different angles to move in
angles = [0, 90, 180, 270]

randomTurtle.pensize(25)
randomTurtle.speed(10)


def random_walk(turtle):
    """The turtle chooses a random path to move in."""
    for steps in range(250):
        turtle.pencolor(random_color())
        selection = choice(moves)
        if selection == "forward":
            turtle.forward(40)
        elif selection == "left":
            turtle.left(choice(angles))
            turtle.forward(40)
        elif selection == "backward":
            turtle.backward(40)
        else:
            turtle.right(choice(angles))
            turtle.forward(40)

    screen = Screen()
    screen.exitonclick()


random_walk(randomTurtle)
