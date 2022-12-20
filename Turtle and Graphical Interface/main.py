from turtle import Turtle, Screen
import turtle as t 


timmy = Turtle()
timmy.shape("turtle")


# count = 0 
# while count < 4:
#     timmy.forward(100)
#     timmy.right(90)
#     count += 1 

# for i in range(4):
#      timmy.forward(100)
#      timmy.right(90)


# import heroes
# print(heroes.gen())

# ------------------------------------------------------- Making Dashed lines --------------------------------------------
# count = 0 
# while count <50: 
#     timmy.forward(5)
#     timmy.penup()
#     timmy.forward(5)
#     timmy.pendown()
#     count += 1 

# for i in range (50):
#     timmy.forward(5)
#     timmy.penup()
#     timmy.forward(5)
#     timmy.pendown()

#------------------------------different shapes ---------------------------# 

# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         timmy.forward(100)
#         timmy.right(angle)


# for shape_side_num in range (3, 11):
#     draw_shape(shape_side_num)

#---------------------- Generating random walk with random color -----------------------------#

import random 
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b )
    return random_color

directions = [0, 90, 180, 270]

timmy.pensize(15)
timmy.speed("fastest") 

for i in range (400):
    timmy.color(random_color())
    timmy.forward(30)
    timmy.setheading(random.choice(directions))














screen = Screen()
screen.exitonclick()

