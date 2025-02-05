from flask import Flask, render_template, url_for, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["POST"])
def post():
    data_json = request.form
    #return data_json
    return render_template("info.html", json=data_json)


if __name__ == "__main__":
    app.run(debug=True)
