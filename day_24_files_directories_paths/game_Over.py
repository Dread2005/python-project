from turtle import Turtle
Aline = "center"
Font = ("courier", 14, "normal")


class GAME_OVER(Turtle):

    def __init__(self):
        super().__init__()
        self.scores = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(x=0, y=-250)
        self.write(arg="GAME OVER!!!", align=Aline , font= Font)