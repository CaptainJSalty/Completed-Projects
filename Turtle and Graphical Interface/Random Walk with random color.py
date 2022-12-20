from turtle import Turtle, Screen
import turtle as t 
import random


timmy = t.Turtle() 
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