from turtle import Turtle, Screen
t_turtle = Turtle()
screen = Screen()

def move_forward():
    t_turtle.forward(10)

screen.listen()

screen.onkey(key="w", fun=move_forward)
# screen.onkey is a higher order function because it takes another function(move_forward)
# when adding a function to another function the () should not be added
# use keyword arguments rather than positional arguments my_function(a= , b= , c=)

screen.exitonclick()

