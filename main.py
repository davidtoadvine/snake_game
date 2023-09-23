from turtle import Screen
from snake import Snake
from food import Food
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Sneaky Snek")
screen.tracer(0)

snake = Snake()
food = Food()
snake.create_snake()
food.create_food()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")


game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.xcor() == 300:
        game_on = False
    if snake.head.xcor() == -300:
        game_on = False
    if snake.head.ycor() == 300:
        game_on = False
    if snake.head.ycor() == -300:
        game_on = False

    for seg in range(len(snake.segments)-1,0,-1):
        if snake.head.xcor() == snake.segments[seg].xcor:
            game_on = False



screen.exitonclick()

