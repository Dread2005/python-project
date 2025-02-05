import random
import turtle
from turtle import Turtle, Screen
turtle.colormode(255)


# ###to import everything have a * after import###
# ###eg: from random import *(Try to avoid this)###

# ### you can import a module as an alias(a)
# ### eg: import turtle as t_turtle

# ### installing modules ###
# go to PyPi
# type in import[module]
#

screen = Screen()
t_turtle = Turtle()

# for _ in range(20):
# t_turtle.forward(10)
# t_turtle.pendown()
# t_turtle.forward(10)
# t_turtle.penup()

# def MakeShape(sides):
#   for _ in range(sides):
#     t_turtle.forward(100)
#      t_turtle.left(360/sides)


# for shape_side in range(3, 11):
#   t_turtle.color(random.choice(colors))
#  MakeShape(shape_side)

#directions = (0, 90, 180, 270)
#t_turtle.pensize(6)

# ###Python Tuples### # a python tuple looks like; (1,2,3) tuples are ordered my_tuple = (9,12,38) to get a specific
# object in a tuple: my_tuple[0] = 9 a tuple can not be changed further in the code, unless changing the actual
#(or change the tuple to a list (list(my_tuple))


def rand_colour():
    r = random.randint(0, 255)
    b = random.randint(0, 255)
    g = random.randint(0, 255)
    rgb_randcolor = (r, g, b)
    return rgb_randcolor

#def randomwalk():
 #   for _ in range(700):
  #      t_turtle.color((rand_colour()))
   #     t_turtle.speed(0)
    #    t_turtle.forward(50)
     #   t_turtle.left(random.choice(directions))
      #  t_turtle.forward(10)
       # t_turtle.left(random.choice(directions))
print(360/5)

t_turtle.speed(0)

def spirograph (size_of_gap):
    for _ in range (int(360/size_of_gap)):
        t_turtle.color((rand_colour()))
        t_turtle.circle(100)
        t_turtle.setheading((t_turtle.heading() + size_of_gap))


spirograph(5)

screen.exitonclick()
