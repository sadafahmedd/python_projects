import turtle
from turtle import Turtle, Screen
import random
# import colorgram
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     tuple = (r,g,b)
#     rgb_colors.append(tuple)
turtle.colormode(255)
list = [(246, 242, 244), (202, 164, 110),  (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

cursor = Turtle()

def art():
    cursor.penup()
    cursor.hideturtle()
    cursor.speed("fastest")
    cursor.setpos(-250, -250)
    x = 10
    while x > 0:
        for _ in range(10):
            cursor.color(random.choice(list))
            cursor.dot(20)
            cursor.penup()
            cursor.forward(50)
        cursor.left(90)
        cursor.forward(50)
        cursor.left(90)
        cursor.forward(500)
        cursor.left(180)
        x = x-1

art()
screen = Screen()
screen.exitonclick()