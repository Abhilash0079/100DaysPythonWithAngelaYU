import turtle as t

dash_turtle = t.Turtle()

# Draw the dash line
for _ in range(15):
    t.forward(10)
    t.penup()
    t.forward(10)
    t.pendown()

# End of code #

screen = t.Screen()
screen.exitonclick()
