from flask import Flask, render_template
import random
import datetime

app = Flask(__name__)


@app.route("/")
def home():
    ### random number gen ###
    random_number = random.randint(1, 10)

    ### copyright footer ###
    year = datetime.date.today()
    list_year = str(year).split("-")
    str_year = list_year[0]

    ### my name ###
    name = "Chiyedza Ford"
    return render_template("index.html", num=random_number, name=name, yr=str_year)


if __name__ == "__main__":
    app.run(debug=True)


#adding {{insert argument}} will register what you wrote between the brackets as python code rather than a string

#when using classes in html, create it in the server, and use key_word_arguments in the render_template part of the code (never forget args and kwargs)
#there needs to be both a name and value, the reason the name is important because the name can be used as a reference inside the templated html file
#in the html write {{kwarg name}} to pass the kwarg from the python file to the html file

