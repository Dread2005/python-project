from turtle import Turtle

Font = ("courier", 30, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.user_score = 0
        self.comp_score = 0

    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(arg=self.user_score, align="center", font=Font)
        self.goto(100, 200)
        self.write(arg=self.comp_score, align="center", font=Font)

    def user_score_add(self):
        self.user_score += 1
        self.update_score()
        #self.update()

    def comp_score_add(self):
        self.comp_score += 1
        self.update_score()



