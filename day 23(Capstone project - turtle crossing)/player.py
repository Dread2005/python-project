from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280



class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)
        self.shape("turtle")
        self.color("brown")

    def move_up(self):
        newY = self.ycor() + MOVE_DISTANCE
        self.goto(x=self.xcor(), y=newY)

    def move_down(self):
        newY = self.ycor() - MOVE_DISTANCE
        self.goto(x=self.xcor(), y=newY)

    def move_left(self):
        newx = self.xcor() - MOVE_DISTANCE
        self.goto(x=newx, y=self.ycor())

    def move_right(self):
        newx = self.xcor() + MOVE_DISTANCE
        self.goto(x=newx, y=self.ycor())

    def reset_(self):
            self.clear()
            self.goto(STARTING_POSITION)

    def is_player_there(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False





