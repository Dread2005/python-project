from turtle import Turtle, Screen
x_side = range(-390, 0)
y_side = range(0, 390)
up = 90
down = 270


class Paddel(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(pos)

    def up(self):
        newyup = self.ycor() + 28
        self.goto(x=self.xcor(), y=newyup)

    def down(self):
        newydown = self.ycor() - 28
        self.goto(x=self.xcor(), y=newydown)







