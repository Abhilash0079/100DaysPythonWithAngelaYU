from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
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
# 5a. Create the scoreboard on the screen
scoreboard = Scoreboard()

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
        # 7a. Extend the snake
        snake.extend()
        # 5b. Increase the score
        scoreboard.increase_score()

    # 6. Detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.reset()
        snake.reset_snake()
        # game_is_on = False
        # scoreboard.game_over()

    # 7b. Detect collision with tail if head collides with any segment in the tail, trigger the game_over
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset_snake()
            # game_is_on = False
            # scoreboard.game_over()

screen.exitonclick()
