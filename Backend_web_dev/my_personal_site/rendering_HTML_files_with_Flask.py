from flask import Flask, render_template
#import render_template
#to render static files(like png and CSS files) create a "static" directory and keep all static files in there
#create another directory called templates (Flask is a framework, so you have to follow the rules established)

app = Flask("my_personal_site")  #or use __name__


@app.route("/")
def home():
    #rendering an html webpage with an html file
    #create a new html file (Index.html)
    #rather than returning a string, call the render_template method
    #[file_path]/ to get the specific file path
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)

