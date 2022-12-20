# import colorgram


# rgb_colors = []
# colors = colorgram.extract('Still in Progress\Turtle and Graphical Interface\image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b 
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

# print(rgb_colors)

from turtle import Turtle, Screen
import turtle as t 
import random


t.colormode(255)
color_list = [(58, 106, 148), (224, 200, 109), (134, 84, 58), (223, 138, 62), (196, 145, 171), (234, 226, 204), (141, 178, 204), (139, 82, 105), (209, 90, 69), (188, 80, 120), (68, 105, 90), (134, 182, 136), (133, 133, 74), (63, 156, 92), (48, 156, 194), (183, 192, 201), (214, 177, 191), (19, 57, 93), (21, 68, 113), (112, 123, 149), (229, 174, 165), (172, 203, 182), (158, 205, 215), (69, 58, 47), (108, 47, 60), (53, 70, 65), (72, 64, 53)]
timmy = t.Turtle()
timmy.speed("fastest")
timmy.penup()
timmy.hideturtle()
timmy.setheading(135)
timmy.forward(300)
timmy.setheading(0)

number_of_dots = 100

for dot_count in range (1, number_of_dots + 1 ):
    timmy.dot(20, random.choice(color_list))
    timmy.forward(50)

    if dot_count % 10 == 0:
            
        timmy.setheading(270)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(0)

screen = t.Screen()
screen.exitonclick()