from turtle import Screen
from snake import Snake
from food import Food
import time

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)  # Animation control

# 1. Create the snake
snake = Snake()
# 4a. Create the food
food = Food()
# 3. Control the snake
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    # 2. Move the snake
    snake.move()

    # 4b. Detect collision with Food
    if snake.head.distance(food) < 15:
        food.refresh()

screen.exitonclick()
