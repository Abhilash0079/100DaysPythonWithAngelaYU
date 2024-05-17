from turtle import Turtle, Screen


# 1. Create the screen
screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)  # Animation control


# 2. Create the paddle
paddle = Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=5, stretch_len=1)
paddle.penup()
paddle.goto(350, 0)


# 3. Move the paddle up and down
def go_up():
    new_y = paddle.ycor() + 20
    paddle.goto(paddle.xcor(), new_y)


def go_down():
    new_y = paddle.ycor() - 20
    paddle.goto(paddle.xcor(), new_y)


screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")

game_is_on = True

while game_is_on:
    screen.update()


screen.exitonclick()
