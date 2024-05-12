import turtle as t
import random
shape_turtle = t.Turtle()
# Draw the different shape
color = ["green", "red", "orange", "turquoise", "olive", "magenta", "sienna", "dark salmon", "gold"]


def draw_shape(num_sides):
    angles = 360 / num_sides
    for _ in range(num_sides):
        shape_turtle.forward(100)
        shape_turtle.right(angles)


for n in range(3, 11):
    shape_turtle.color(random.choice(color))
    draw_shape(n)

# End of code #

screen = t.Screen()
screen.exitonclick()
