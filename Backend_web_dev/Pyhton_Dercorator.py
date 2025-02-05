from flask import Flask
import time

# app = Flask(__name__)

# @app.route("/")
# #takes us to our "home page"
# #it is called a Python Decorator

# def hello_world():
#     return "<p>Hello, World!</p>"
#
# if __name__ == "__main__":
#     app.run()

#Explenation:
#Decorators functions that give additional functinality to an alrea exsiting function
###########################
###########################
# def add(n1, n2):
#     return n1 + n2
#
# def subtract(n1, n2):
#     return n1 - n2
#
# def multiply(n1, n2):
#     return n1 * n2
#
# def divide(n1, n2):
#     return n1 / n2
#
# ##Functions are first-class objects, can be passed around as arguments e.g. int/string/float etc.
#
# def calculate(calc_function, n1, n2):
#     return calc_function(n1, n2)
#
# result = calculate(add, 2, 3)
# print(result)
#
# ##Functions can be nested in other functions
# def outer_function():
#     print("I'm outer")
#
#     def nested_function():
#         print("I'm inner")
#
#     nested_function()
#
# outer_function()
#
# ## Functions can be returned from other functions
# def outer_function():
#     print("I'm outer")
#
#     def nested_function():
#         print("I'm inner")
#
#     return nested_function
# inner_function = outer_function()
# inner_function()
####################
#####################

# ## Simple Python Decorator Functions:

# def delay_dec(function):
#     def wrapper_function():
#         time.sleep(10)
#         # write here to do something before the function
#         function()
#         function()
#         #or run it twice[function()]
#         #write here to do something after the function
#     return wrapper_function
#
# @delay_dec #this is known as syntactic suger "@" sign, makes it easier and faster
# def say_hello():
#     print("hello")
#
# say_hello()

# #With the @ syntactic sugar
# @delay_decorator
# def say_bye():
#     print("Bye")
#
# #Without the @ syntactic sugar
# def say_greeting():
#     print("How are you?")
# decorated_function = delay_decorator(say_greeting)
# decorated_function()

def dec_function(function):
    def wrapper_function():
        time.sleep(3)
        function()
        time.sleep(3)
        function()
    return wrapper_function

@dec_function
def it_worked_twice():
    print("it worked twice fam")

it_worked_twice()
