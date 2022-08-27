from turtle import Screen
from snake import Snake

import time

SPEED_OF_GAME = 0.1
WALL_POSITION = 280

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Hunting Snake Game")
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(SPEED_OF_GAME)
    snake.move()

    # Detect collision with food.

    # Detect collision with wall.

    # Detect collision with tail.

screen.exitonclick()
