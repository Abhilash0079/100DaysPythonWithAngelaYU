import turtle

square_turtle = turtle.Turtle()
square_turtle.shape("arrow")
square_turtle.color("green")
# Making a square #
for _ in range(4):
    square_turtle.forward(100)
    square_turtle.right(90)

# End of code #

screen = turtle.Screen()
screen.exitonclick()
