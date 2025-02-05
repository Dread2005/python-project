from flask import Flask, render_template, url_for, request
import requests

app = Flask(__name__)

api_endpoint = requests.get("https://api.npoint.io/cff2e24d6fdedb94e663").json()
contact_data = None


@app.route("/")
def home():
    img = '/static/assets/img/home-bg.jpg'
    return render_template("index.html", image=img, json=api_endpoint)


@app.route("/about")
def about():
    img = 'static/assets/img/about-bg.jpg'
    return render_template("about.html", image=img)


@app.route("/contacts")
def contact():
    img = 'static/assets/img/contact-bg.jpg'
    return render_template("contact.html", image=img)


@app.route("/post/<int:index>")
def post(index):
    req = None
    for blog in api_endpoint:
        if blog["id"] == index:
            req = blog
            print(blog)
    return render_template('post.html', json=req)


@app.route("/contact_data", methods=["POST"])
def contact_data():
    return request.form


if "__main__" == __name__:
    app.run(debug=True)
