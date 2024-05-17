from turtle import Turtle


class Ball(Turtle):
    # 5a. Create a ball
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()

    # 5b. Move the ball
    def move(self):
        new_x = self.xcor() + 10
        new_y = self.ycor() + 10
        self.goto(new_x, new_y)
