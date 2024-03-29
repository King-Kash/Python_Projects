import colorgram
import turtle
import random
tim = turtle.Turtle()
# colors = colorgram.extract('hirst.jpg', 30)
# rgb_array = []
#
# for i in range(len(colors)):
#     rgb = colors[i].rgb
#     color_tuple = (rgb.r, rgb.g, rgb.b)
#     rgb_array.append(color_tuple)
#
# print(rgb_array)



turtle.colormode(255)
color_list = [(203, 165, 107), (239, 246, 241), (151, 73, 47), (235, 238, 244), (172, 154, 39), (52, 93, 125), (223, 202, 134), (137, 32, 20), (132, 162, 185), (202, 90, 69), (48, 122, 88), (67, 48, 41), (13, 100, 73), (146, 178, 146), (164, 142, 156), (111, 73, 77), (236, 175, 164), (152, 19, 23), (19, 84, 89), (183, 205, 171), (56, 45, 48), (40, 61, 74), (48, 65, 81), (80, 147, 127), (189, 83, 86), (175, 192, 211), (14, 74, 66), (224, 176, 182)]

tim.speed("fastest")
tim.hideturtle()
tim.up()
tim.goto(-225, -225)
for i in range(10):
    for i in range(10):
        tim.dot(20, random.choice(color_list))
        tim.up()
        tim.forward(50)
    tim.goto(-225, tim.ycor()+50)



screen = turtle.Screen()
screen.exitonclick()