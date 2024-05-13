import turtle as t
import random

spiro_turtle = t.Turtle()
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


spiro_turtle.speed("fastest")


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        spiro_turtle.color(random_color())
        spiro_turtle.circle(100)
        spiro_turtle.setheading(spiro_turtle.heading() + size_of_gap)


draw_spirograph(5)
# End of code #

screen = t.Screen()
screen.exitonclick()
