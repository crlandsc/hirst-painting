###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

import turtle
from turtle import Turtle as T, Screen
import random

tim = T()
tim.color("purple1")

def random_color(color_list):
    color = random.choice(color_list)
    return color

def dot_painting(w,h):
    y_coord = -25*h
    for steps in range(0, h):
        tim.setposition(-25*w,y_coord) # reset the x coord and increment y coord
        for steps in range(0, w):
            color = random_color(color_list)
            tim.pencolor(color)
            tim.dot(20)
            tim.forward(50)
        y_coord += 50

color_list = [(202, 164, 110), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41),
              (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149),
              (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171),
              (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64),
              (107, 127, 153), (176, 192, 208), (168, 99, 102)]
turtle.colormode(255)
tim.speed(0)
tim.pu() # pen up - don't draw line
tim.hideturtle()

# Run dot painting code


dot_painting(12,12)


screen = Screen()
screen.exitonclick()