from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("green")
        self.speed(0)
        rand_x = random.randint(-290, 290)
        rand_y = random.randint(-290, 290)
        self.goto(x=rand_x, y=rand_y)

    def refresh(self):
        rand_x = random.randint(-290, 290)
        rand_y = random.randint(-290, 290)
        self.goto(x=rand_x, y=rand_y)

