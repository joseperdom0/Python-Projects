import turtle
import random

tim = turtle.Turtle()
win = turtle.Screen()

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
angles = [0, 90, 180, 270]


def walk_randomly(random_colour, random_angle):
    tim.setheading(random_angle)
    tim.color(random_colour)
    tim.forward(20)


tim.speed(0)
tim.width(2)
for _ in range(10000):
    colour = random.choice(colours)
    angle = random.choice(angles)
    walk_randomly(colour, angle)


win.exitonclick()

# TODO keep it inside canvas

