from flask import Flask, render_template, url_for, request
import requests
import smtplib

# USE YOUR OWN npoint LINK! ADD AN IMAGE URL FOR YOUR POST. 👇
posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
My_email = "tshifhiwachedzafordjr@gmail.com"
Pass = "qjba mlqf pfrc ghox"

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["POST", "GET"])
def contact():
    if request.method == "POST":
        jsn = request.form
        name = jsn["name"]
        email = jsn["email"]
        phone = jsn["phone"]
        msg = jsn["message"]

        with smtplib.SMTP("smtp.gmail.com", port=587) as connect:
            connect.starttls()
            connect.login(user=My_email, password=Pass)
            connect.sendmail(
                from_addr=My_email,
                to_addrs=My_email,
                msg=f"Subject:Message from contacts page\n\n"
                    f"{name}\n"
                    f"{email}\n"
                    f"{phone}\n"
                    f"{msg}")
    return render_template("contact.html")


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


# @app.route("/data-entry", methods=["POST"])
# def receive_data():
#     jsn = request.form
#     name = jsn["name"]
#     email = jsn["email"]
#     phone = jsn["phone"]
#     msg = jsn["message"]
#     print(f"{name}\n{email}\n{phone}\n{msg}")
#     return f"<h1> Successfully sent </h1>"


if __name__ == "__main__":
    app.run(debug=True, port=5001)
