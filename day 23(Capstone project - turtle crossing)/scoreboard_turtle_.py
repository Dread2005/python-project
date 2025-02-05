from turtle import Turtle
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(x=-230, y=270)
        self.update_()

    def update_(self):
        self.clear()
        self.write(arg=f"level: {self.level}", align="center", font=FONT)

    def next_level(self):
        self.level += 1
        self.update_()

    def game_over(self):
        self.color("red")
        self.level = 0
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=0)
        self.write(arg=f"Game Over!!!", align="center", font=FONT)


