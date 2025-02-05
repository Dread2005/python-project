from flask import Flask
#Flask is a FRAMEWORK

app = Flask(__name__)
#__name__ is a special attribute to find out the current class, function method ect
#print(__name__)
#__main__ means we are executing the code in a scope, __main__ is the file being run


@app.route("/")
#takes us to our "home page"
#it is called a Python Decorator
def hello_world():
    return "<p>Hello, World!</p>"


if __name__ == "__main__":
    app.run() # this is the same as the method underneath without opening the terminal

###running a flask app:
#create a venv in terminal:
# PS C:\Users\Tshifhiwa\Downloads\wetransfer_python_stuffs_2024-04-27_1325\backend_web_dev> python3 -m venv .venv
# PS C:\Users\Tshifhiwa\Downloads\wetransfer_python_stuffs_2024-04-27_1325\backend_web_dev> .venv\Scripts\activate

#go to terminal
#type- set FLASK_APP=[insert file name.py]
#then use the flask command- "flask run"
