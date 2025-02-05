import requests
from flask import Flask, render_template
from post import Post


app = Flask(__name__)

post_obj = []

api_endpoint = "https://api.npoint.io/cff2e24d6fdedb94e663"

response = requests.get(url=api_endpoint)
answer = response.json()
print(answer)
for post in answer:
    pst = Post(post["id"], post["title"], post["subtitle"], post["body"], post["date"], post["author"], post["image_url"])
    post_obj.append(pst)


@app.route("/")
def home():
    img = 'home-bg.jpg'
    return render_template("index.html", image=img, json=post_obj)


@app.route("/abouts")
def about():

    img = 'about-bg.jpg'
    return render_template("about.html", image=img, )


@app.route("/contacts")
def contact():

    img = 'contact-bg.jpg'
    return render_template("contact.html", image=img)


@app.route("/posts/<int:index>")
def posts(index):
    req_post = None
    img = None
    for ans in post_obj:
        if ans.id == index:
            req_post = ans
            img = req_post.image
    return render_template("post.html", post=req_post, image=img)


if __name__ == "__main__":
    app.run(debug=True)

