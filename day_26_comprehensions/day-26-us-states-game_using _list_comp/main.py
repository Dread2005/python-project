import turtle
import pandas

data = pandas.read_csv("50_states.csv")
screen = turtle.Screen()
image = "blank_states_img.gif"
screen.setup(width=725, height=491)
screen.title("Us states game")
screen.addshape(image)
turtle.shape(image)

score = 0
print(len(data["state"]))
guessd_states = []

playing = True
while playing:

    user_answer = screen.textinput(title=f"({score}/50) what is you're choice:", prompt="enter").title()
    states = data.state.to_list()

    if user_answer == "Exit":
        missing_states = [state for state in states if state not in guessd_states]
        learn_data = pandas.Series(missing_states)
        learn_data.to_csv("need_to_learn")
        print(missing_states)
        break

    if user_answer in states:
        state_data = data[data.state == user_answer]
        x = int(state_data.x)
        y = int(state_data.y)
        print(user_answer)
        write = turtle.Turtle()
        write.penup()
        write.hideturtle()
        write.color("black")
        write.goto(x=x, y=y)
        # panda.item, takes a specific item from the csv you are using 
        write.write(state_data.state.item())
        guessd_states.append(state_data.state.item())
        score += 1
    if score == 50:
        playing = False
screen.exitonclick()


