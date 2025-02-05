import random
from turtle import Turtle, Screen

race_on = False
screen = Screen()
screen.setup(width=800, height=600)
screen.listen()
user_bet = screen.textinput(title="place ur bet",prompt="enter ur bet")
print(user_bet)
#state(performing different methods at any one time)

colours = ["red", "green", "yellow", "blue", "purple", "orange"]
y_positions = [-20, -80, -140, -180, -240, 40]
all_turtles = []


for turtles in range(0, 6):
    new_turtle = Turtle()
    new_turtle.shape("turtle")
    new_turtle.penup()
    new_turtle.goto(x=-390, y=y_positions[turtles])
    new_turtle.color(colours[turtles])
    all_turtles.append(new_turtle)
race_on = True

while race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 400:
            race_on = False
            if user_bet == turtle.color()[1]:
                print(f"You won the {turtle.color()[1]} turtle got there first")
            else:
                print(f"You lost {turtle.color()[1]} won")
        rand_forward = random.randint(0, 25)
        turtle.forward(rand_forward)



screen.exitonclick()
