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


timmy.speed("fastest")

def draw (size_gap):
    for i in range(int(360/size_gap)): 
        timmy.color(random_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + size_gap)

draw(5)

screen = t.Screen()
screen.exitonclick()