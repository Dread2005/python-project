from flask import Flask

########Passing A URL##########
app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello world"


#to go to the "Bye" rute, once on the web browser type /[insert name]
@app.route("/bye")
def bye():
    return "Bye"


#########Variable Rules##########
#we can create a variable[something you can input] in a URL by marking it with <[insert variable name]>

#path before:/username/<name> or just path: "/<name>" or add paths afterwords: "/<name>"/surname/<surname>/
#@app.route("/username/<name>/surname/<surname>")

#or use the converter: <[converter type]: [variable name]>
#converter types: string(default), int, path, float, uuid
@app.route("/<name>/<int:number>")
def greet(name, number):
    return f"Hello there mr {name}, age:{number}"


if __name__ == "__main__":
    ####### debugger #####
    #putting debugger on:
    app.run(debug=True)
