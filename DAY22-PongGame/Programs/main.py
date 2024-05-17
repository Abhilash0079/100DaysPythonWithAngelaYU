from turtle import Screen
from paddle import Paddle

# 1. Create the screen
screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)  # Animation control


# 2. Create the paddle
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

# 3. Control the paddle
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True

while game_is_on:
    screen.update()


screen.exitonclick()
