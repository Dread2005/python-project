from turtle import Screen
from pong_padle import Paddel
import time
from pong_ball import PongBall
from words_on_screen import write
from score_board_pong import Score

goals = [-370, 370]

time = time

position = [(-360, 0), (360, 0)]

speed = [0, 0.1, 0.0, 0.01, 0.02, 0.03]
score = Score()

screen = Screen()


screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("pong")

user_paddel = Paddel(position[1])
comp_paddel = Paddel(position[0])


screen.listen()
screen.onkey(fun=user_paddel.up, key="w")
screen.onkey(fun=user_paddel.down, key="s")
screen.onkey(fun=comp_paddel.up, key="i")
screen.onkey(fun=comp_paddel.down, key="k")

ball = PongBall()

score.update_score()

playing = True
while playing:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move_ball()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    if ball.distance(user_paddel) < 50 and ball.xcor() > 340:
        ball.bounce_x()
        print("touch")
        for n in speed:
            time.sleep(n)

    if ball.distance(comp_paddel) < 50 and ball.xcor() < -340:
        ball.bounce_x()
        print("touch")

    if ball.xcor() < goals[0]:
        score.comp_score_add()
        ball.reset()
        time.sleep(2)

    if ball.xcor() > goals[1]:
        score.user_score_add()
        ball.reset()
        time.sleep(2)





















screen.exitonclick()
