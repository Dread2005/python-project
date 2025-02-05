from flask import Flask
import random

app = Flask(__name__)

random_int = random.randint(0, 9)


@app.route("/")
def home():
    return ("<h1> Guess a number between 0 and 9 </h1>"
            "<img src=https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif>")


@app.route("/<int:number>")
def results(number):
    if number < random_int:
        return ("<h1 style = 'color: red'> too low <h1>"
                "<img src=https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExazZyZnM3NndoZ3liaWF2OXV2ZTJrYjFzbzB0ZXY0YzM4bGlkMDNsZCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3oz8xsuGvBn03H1boY/giphy.webp>")
    elif number > random_int:
        return ("<h1 style = 'color: yellow'> Too high </h1>"
                "<img src=https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExMWZzZzE2N2p6Mmg5MDc3bWRoc3MzYXU3ajh3dWdrZzkwcWg2c28xMCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/vyTnNTrs3wqQ0UIvwE/giphy.webp>")
    else:
        if number == random_int:
            return ("<h1 style = 'color: green'> Perfect </h1>"
                    "<img src=https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExaTBqMnh5cWZ1ZnM3MjdzNGNocWZiNTN1M3FpM2I4ZHV2eWl5bGJyNCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/WJjLyXCVvro2I/giphy.webp>")

    input_ = input("type 'end' when ready to finish: ")


if __name__ == "__main__":
    app.run(debug=True)
