from flask import Flask, render_template
import requests
from post import Post

post_obj = []
posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
for post in posts:
    pst = Post(post["id"], post["title"], post["subtitle"], post["body"])
    post_obj.append(pst)

# for n in post_obj:
#     print(n.title)

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html", post=post_obj)


@app.route('/post/<int:index>')
def blog_(index):
    req_post = None
    for post_ in post_obj:
        if post_.id == index:
            req_post = post_

    return render_template("post.html", pst=req_post)




if __name__ == "__main__":
    app.run(debug=True)
