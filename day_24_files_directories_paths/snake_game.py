import turtle
from score_bored import ScoreBoard
from the_snake import Snake
from food import Food
from turtle import Screen
from game_Over import GAME_OVER
import time



screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
screen.listen()
food = Food()
score_board = ScoreBoard()
game_over = GAME_OVER

screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.right, "d")
screen.onkey(snake.left, "a")

on = game_is_running = True

while game_is_running:
    screen.update()
    time.sleep(0.1)
    snake.move()
# detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.append()
        score_board.increase_score()

    #detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -285:
        score_board.reset()
        time.sleep(1.5)
        snake.reset()
        #game_over()

    elif snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score_board.reset()
        time.sleep(1.5)
        snake.reset()
        #game_over()

    for segments in snake.segments[1:]:
        if snake.head.distance(segments) < 10:
            score_board.reset()
            time.sleep(1.5)
            snake.reset()
            #game_over()
    #detect collision with tailw
    # if head hits the body
    #game = over

### SLICING ###
#piano_keys [a, b, c, d, e , f, g]
#slicing piano_keys[2:5]
# 2 = c and 5 = f
#piano_keys [2:5] are piano_keys c, d, e
# this sign : is what's used to slice the list
#[2:] gives the whole list from 2

#piano_keys[2:5:2]
#piano_keys c, e
#the third number is what it counts in, in this eg its slicing from 2 to 5 in 2s

# [::-1] reverses the whole list





screen.exitonclick()


































screen.exitonclick()