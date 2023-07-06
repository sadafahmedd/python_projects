from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score
import time
# Setting up screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

# STEP 1 : Creating the Snake body

snake = Snake()
food = Food()
score = Score()

# STEP 3: Keyboard controls
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# STEP 2 : Moving the snake
# Code to move snake forward
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # Detecting collision with food

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase()

    # Detect collision with wall

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.reset()
        snake.reset()

    # Detect collision with tail

    for segment in snake.snake_body[1:]:
        if snake.head.distance(segment) < 10:
            score.reset()
            snake.reset()






screen.exitonclick()
