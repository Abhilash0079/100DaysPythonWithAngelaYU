from turtle import Turtle


class Ball(Turtle):
    # 5a. Create a ball
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10

    # 5b. Move the ball
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    # 6. Bouncing the ball when collision with wall
    def bounce_y(self):
        self.y_move *= -1

    # 7. Detect collision with paddle.
    def bounce_x(self):
        self.x_move *= -1
