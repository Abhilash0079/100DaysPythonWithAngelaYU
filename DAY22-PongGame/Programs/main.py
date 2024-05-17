from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

# 1. Create the screen
screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)  # Animation control


# 2. Create the paddle
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

# 5a. Create a ball
ball = Ball()

# 3. Control the paddle
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    # 5b. Move the ball
    ball.move()

    # 6. Detect the collision with the wall.
    if ball.ycor() > 280 or ball.ycor() < -280:
        # need to bounce
        ball.bounce_y()

    # 7. Detect collision with paddle.
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    # 8a. Detect when right paddle misses the ball.
    if ball.xcor() > 380:
        ball.reset_position()

    # 8b. Detect when left paddle misses the ball.
    if ball.xcor() < -380:
        ball.reset_position()

screen.exitonclick()
