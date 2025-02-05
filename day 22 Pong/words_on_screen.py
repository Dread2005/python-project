from turtle import Turtle
Font = ("courier", 14, "normal")

class write(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 280)
        self.write(arg="SCORE!!!!", align="center", font=Font)