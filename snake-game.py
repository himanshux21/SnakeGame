from turtle import Screen
import time
from food import Food
from new_snake import Snake
from scoreboard import ScoreBoard
screen = Screen()
screen.setup(600, 600)
screen.bgcolor('black')
screen.title('My Snake Game')
screen.tracer(0)
score = ScoreBoard()
screen.update()
food = Food()
snake = Snake()
screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.right, 'Right')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.down, 'Down')
game_on = True
while game_on:
    screen.update()
    time.sleep(0.2)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend_segment()
        score.increase_score()
    for seg in snake.segments[1:]:
        if snake.head.distance(seg) < 10:
            score.game_over()
            game_on = False
    if snake.head.xcor() <= -295 or snake.head.xcor() >= 295 or snake.head.ycor() <= -295 or snake.head.ycor() >= 295:
        score.game_over()
        break
screen.exitonclick()
