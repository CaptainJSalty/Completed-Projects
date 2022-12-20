from turtle import Turtle, Screen
import turtle as t 
import random

timmy = Turtle()
timmy.shape("turtle")
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b )
    return random_color


def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        timmy.forward(100)
        timmy.right(angle)
        timmy.color(random_color())


for shape_side_num in range (3, 11):
    draw_shape(shape_side_num)


screen = Screen()
screen.exitonclick()