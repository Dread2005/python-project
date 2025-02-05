from turtle import Turtle, Screen
import time
co_or = [(0, 0), (-20, 0), (-40, 0)]
screen = Screen()
up = 90
down = 270
left = 180
right = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for pos in co_or:
            self.add_segments(pos)

    def add_segments(self, pos):
        new_snake = Turtle()
        new_snake.penup()
        new_snake.pencolor("black")
        new_snake.color("white")
        new_snake.shape("square")
        new_snake.goto(pos)
        self.segments.append(new_snake)



    def append(self):
        self.add_segments(self.segments[-1].position())

    def move(self):
        # for visualisation (for seg_num in range(start=2, stop=0, step=-1):)
        for seg_num in range(len(self.segments) - 1, 0, -1):
            newx = self.segments[seg_num - 1].xcor()
            newy = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(x=newx, y=newy)
        self.head.forward(20)

    def right(self):
        if self.head.heading() != left:
            self.head.setheading(right)

    def left(self):
        if self.head.heading() != right:
            self.head.setheading(left)

    def up(self):
        if self.head.heading() != down:
            self.head.setheading(up)

    def down(self):
        if self.head.heading() != up:
            self.head.setheading(down)




