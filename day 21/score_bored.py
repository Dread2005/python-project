from turtle import Turtle
Aline = "center"
Font = ("courier", 14, "normal")
class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.scores = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(x=0, y=270)
        self.write(arg=f"score:{self.scores}", align=Aline , font= Font)


    def update(self):
        self.write(arg=f"score:{self.scores}", align=Aline, font=Font)

    def increase_score(self):
        self.scores += 1
        self.clear()
        self.update()
