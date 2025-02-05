from turtle import Turtle, Screen

t_turtle = Turtle()
screen = Screen()


def move_forward():
    t_turtle.forward(10)


def move_back():
    t_turtle.back(10)


def turn_left():
    t_turtle.left(10)


def turn_right():
    t_turtle.right(10)


def clear():
    t_turtle.penup()
    t_turtle.home()
    t_turtle.clear()
    t_turtle.pendown()



screen.listen()
screen.onkey(fun=move_forward, key="w")
screen.onkey(fun=move_back, key="s")
screen.onkey(fun=turn_left, key="a")
screen.onkey(fun=turn_right, key="d")
screen.onkey(fun=clear, key="c")


screen.exitonclick()


