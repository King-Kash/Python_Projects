import turtle
from turtle import Turtle, Screen
import random
#this is how you import stuff using an alia. You may want to use an alias if the name of a module is long
#import turtle as t
#tim = t.Turtle()

#if you uncomment the line below and click on the red bulb you will be prompted to install a module that
#does not come in the python standard library
#import heroes
turtle.colormode(255)
tim = Turtle()
colors = ["Red", "Orange", "Yellow", "Green", "Blue", "Indigo", "Violet", "Fuchsia", "Aqua", "Lime"]
directions = [0, 90, 180, 270, -90, -180, -270]
#-90, -180, -270

# numSides = 3
# while numSides < 10:
#     tim.color(random.choice(colors))
#     for i in range(numSides):
#         tim.forward(100)
#         tim.right(360/numSides)
#     numSides += 1


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)
#
tim.speed("fastest")
# for i in range(100):
#     angle = random.choice(directions)
#     tim.color(random_color())
#     tim.setheading(angle)
#     tim.forward(25)

num_circles = 100
for i in range(num_circles):
    tim.color(random_color())
    tim.circle(100,360,50)
    tim.left(360/num_circles)

tim_orientation = tim.heading()
















screen = Screen()
screen.exitonclick()
