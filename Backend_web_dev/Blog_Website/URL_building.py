#url building means to create a link on the page linking to another page
#use an anchor tag <a href = "{{url_for(<'item in flask file'>[like home():]}}"> </a>
#you can add parameters same way you do with render_template with **Kwargs in HTML

import requests
from flask import Flask, render_template

#name = input("Enter name: ")

app = Flask(__name__)


@app.route("/")
def first_url():
    return "got to /blog"


@app.route("/home")
def home():
    return render_template("index.html")


@app.route("/blog/<num>")
def blog(num):
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    re_json = response.json()
    return render_template("blog_website.html", post=re_json)


if __name__ == "__main__":
    app.run(debug=True)

