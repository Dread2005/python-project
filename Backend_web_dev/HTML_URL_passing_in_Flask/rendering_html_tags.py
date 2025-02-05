from flask import Flask


def bold_dec(function):
    def wrapp():
        #you need to return it or else nothing will show up
        return "<b>" + function() + "<b>"

    return wrapp


def underline(function):
    def wrapper():
        return "<u>" + function() + "<u>"

    return wrapper


def italics(function):
    def wrapper():
        return "<i>" + function() + "</i>"

    return wrapper


app = Flask(__name__)


@app.route("/")
def hello_world():
    #you can add html in the return to have html in your actual website
    #you can add css too(style)
    return "<h1 style='text-align: center'>Midzi wellness</h1>"\
            "<p style='text-align: center'>start of business website</p>"\
            "<img src=https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExNGY1OGhpZ3VrYnQ2OG44em94NWFqMGIzN3A3dHE2MHo4ZzVveHlsOCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/tkJsL5AIIsg7K/giphy.webp width=1180> length=900"


@app.route("/bye")
@bold_dec
@underline
@italics
def bye():
    return "Bye"


@app.route("/<name>/<int:number>")
def greet(name, number):
    return f"Hello there mr {name}, age:{number}"


if __name__ == "__main__":
    app.run(debug=True)
