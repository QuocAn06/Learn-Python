from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

SPEED_OF_GAME = 0.1
WALL_POSITION = 290

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Hunting Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

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
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall.
    if snake.head.xcor() > WALL_POSITION or snake.head.xcor() < -WALL_POSITION:
        scoreboard.reset()
        snake.reset()
        food.refresh()

    if snake.head.ycor() > WALL_POSITION or snake.head.ycor() < -WALL_POSITION:
        scoreboard.reset()
        snake.reset()
        food.refresh()

    # Detect collision with tail.
    for seg in snake.segments[1:]:
        if snake.head.distance(seg) < 10:
            scoreboard.reset()
            snake.reset()
            food.refresh()

screen.exitonclick()
