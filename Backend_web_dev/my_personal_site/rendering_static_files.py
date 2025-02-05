from flask import Flask, render_template
#import

app = Flask("my_personal_site")  #or use __name__


@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
