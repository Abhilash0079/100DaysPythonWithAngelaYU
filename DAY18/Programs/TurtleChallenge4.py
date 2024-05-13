import turtle as t
import random
shape_turtle = t.Turtle()
# Draw the randon walk
t.colormode(255)
# color = ["green", "red", "orange", "turquoise", "olive", "magenta", "sienna", "dark salmon", "gold"]
direction = [0, 90, 180, 270]
t.pensize(15)
t.speed("fastest")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

for _ in range(200):
    t.forward(30)
    t.setheading(random.choice(direction))
    t.color(random_color())

# End of code #

screen = t.Screen()
screen.exitonclick()
