from turtle import Turtle
Aline = "center"
Font = ("courier", 14, "normal")
class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.content = int(data.read())
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(x=0, y=270)
        self.write(arg=f"score:{self.score}             high_score:{self.content}", align=Aline , font= Font)

    def update(self):
        self.clear()
        self.write(arg=f"score:{self.score}             high_score:{self.content}", align=Aline, font=Font)

    def increase_score(self):
        self.score += 1
        self.update()

    def reset(self):
        if self.score > self.content:
            self.content = self.score
            with open("data.txt", "w") as file:
                file.write(f"{self.content}")
        self.score = 0
        self.update()


