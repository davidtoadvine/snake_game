from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

BORDER = 290

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Sneaky Snek")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # check for food eaten
    if snake.head.distance(food) < 15:
        scoreboard.increase_score()
        snake.extend()
        food.refresh()

    # check for wall collision
    if snake.head.xcor() > BORDER or snake.head.xcor() < -BORDER or snake.head.ycor() > BORDER or snake.head.ycor() < -BORDER:
        scoreboard.game_over()
        game_on = False

    # check for self collision
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.game_over()
            game_on = False

screen.exitonclick()
