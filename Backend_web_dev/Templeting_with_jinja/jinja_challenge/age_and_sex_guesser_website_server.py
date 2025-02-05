import requests
from flask import Flask, render_template

#name = input("Enter name: ")

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello, please type your name at the end of the url and hit enter "


@app.route("/<name>")
def age_gender_gusser(name):
    my_name = {
        "name": name
    }
    age_response = requests.get("https://api.agify.io?", params=my_name)
    age_json = age_response.json()
    age = age_json["age"]
    #print(age)

    sexuality_response = requests.get("https://api.genderize.io?", params=my_name)
    sexuality_json = sexuality_response.json()
    gender_guesser = sexuality_json["gender"]
    probability_counter = sexuality_json["probability"]
    #print(f"age:{age}, Gender:{gender_guesser}, gender_probability:{probability_counter}")
    return render_template("index.html", age=age, gender=gender_guesser)


if __name__ == "__main__":
    app.run(debug=True)

    

