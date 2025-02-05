from flask import Flask, render_template, request, redirect, url_for


'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)

all_books = []
amount_of_books = int(len(all_books))


@app.route('/')
def home():
    return render_template("index.html", books=all_books, list_leng=amount_of_books)


@app.route("/add",  methods=["POST", "GET"])
def add():
    if request.method == "POST":
        book_details = {
             "title": request.form["book"],
             "author": request.form["author"],
             "rating": f"{request.form['rating']}/10"}
        all_books.append(book_details)
        print(all_books)
    return render_template("add.html",)


if __name__ == "__main__":
    app.run(debug=True)

