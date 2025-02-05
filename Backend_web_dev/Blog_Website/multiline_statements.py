#single line statements in jinja templating looks like {{<line of python code>}}:

#used in the HTML file
#used to recognize python code in html
#its jinja templating

#double line statments like "if" and "while" in jinja templeting looks like: {% for statement %} and to end the if statement use {% endfor %}
#look at blog_website.html for examples

import requests
from flask import Flask, render_template

#name = input("Enter name: ")

app = Flask(__name__)


@app.route("/")
def home():
    return "Blog site home"


# @app.route("/<name>")
# def age_gender_gusser(name):
#     my_name = {
#         "name": name
#     }
#     age_response = requests.get("https://api.agify.io?", params=my_name)
#     age_json = age_response.json()
#     age = age_json["age"]
#     #print(age)
#
#     sexuality_response = requests.get("https://api.genderize.io?", params=my_name)
#     sexuality_json = sexuality_response.json()
#     gender_guesser = sexuality_json["gender"]
#     probability_counter = sexuality_json["probability"]
#     #print(f"age:{age}, Gender:{gender_guesser}, gender_probability:{probability_counter}")
#     return render_template("index.html", age=age, gender=gender_guesser)

@app.route("/blog")
def blog():
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    re_json = response.json()
    return render_template("blog_website.html", post=re_json)


if __name__ == "__main__":
    app.run(debug=True)