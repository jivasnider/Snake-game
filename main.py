from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Super Snake Game")
screen.tracer(0)
screen.listen()

snake = Snake()
food = Food()
score = Scoreboard()
screen.onkey(fun=snake.go_north, key="w")
screen.onkey(fun=snake.go_south, key="s")
screen.onkey(fun=snake.go_east, key="d")
screen.onkey(fun=snake.go_west, key="a")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        print("nom nom nom")
        snake.extend()
        food.refresh()
        score.score_counter()
    if snake.tail_collision():
        game_is_on = False
        score.update_scoreboard()