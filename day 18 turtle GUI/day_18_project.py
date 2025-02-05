import random
import turtle

screen = turtle.Screen()

#spot_colors = colorgram.extract('spots_hirst.jpg', 60)
#spot_rgb = []

#for color in spot_colors:
    #r = color.rgb.r
    #g = color.rgb.g
   # b = color.rgb.b
  #  needed_colors = (r, g, b)
 #   spot_rgb.append(needed_colors)
#print(spot_rgb)

the_colors = [(211, 154, 98), (53, 107, 131), (242, 249, 246), (235, 240, 244), (177, 78, 33), (198, 142, 35), (116, 155, 171), (124, 79, 98), (123, 175, 157), (226, 197, 130), (190, 88, 109), (12, 50, 64), (56, 39, 19), (41, 168, 128), (50, 126, 121), (199, 123, 143), (166, 21, 30), (224, 93, 79), (243, 163, 161), (38, 32, 34), (3, 25, 25), (80, 147, 169), (161, 26, 22), (21, 78, 90), (234, 167, 171), (171, 206, 190), (103, 127, 156), (165, 202, 210), (61, 60, 72), (183, 190, 204), (78, 66, 42), (23, 99, 96)]
d_turtle = turtle.Turtle()
turtle.colormode(255)
d_turtle.setheading(220)
d_turtle.hideturtle()
d_turtle.pencolor("white")
d_turtle.forward(600)
d_turtle.right(220)

def spot_painting():
    for _ in range(25):
        d_turtle.dot(20, random.choice(the_colors))
        d_turtle.pendown()
        d_turtle.penup()
        d_turtle.fd(50)

def turn_left():
    d_turtle.left(90)
    d_turtle.forward(50)
    d_turtle.left(90)
    d_turtle.forward(20)


def turn_right():

    d_turtle.right(90)
    d_turtle.forward(50)
    d_turtle.right(90)
    d_turtle.forward(20)


for _ in range(10):
    spot_painting()
    turn_left()
    spot_painting()
    turn_right()


screen.exitonclick()