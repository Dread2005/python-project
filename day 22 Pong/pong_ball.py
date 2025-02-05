from turtle import Turtle
import time



class PongBall(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.xmove = 10
        self.ymove = 10
        self.move_speed = 0.1

    def move_ball(self):
        newX = self.xcor() + self.xmove
        newY = self.ycor() + self.ymove
        self.goto(x=newX, y=newY)

    def bounce(self):
        self.ymove *= -1

    def bounce_x(self):
        self.xmove *= -1
        self.move_speed *= 0.8

    def reset(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()






