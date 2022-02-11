# 9 columns x 12 rows
# https://www.guyhepner.com/product/flumequine-by-damien-hirst/
import turtle
import random

screen = turtle.Screen()
canvas_width = 425
canvas_height = 550
screen.screensize(canvas_width, canvas_height)
turtle.colormode(255)

tim = turtle.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
dot_size = int(canvas_width * .5 / 9)

color_list = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40),
              (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71),
              (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74),
              (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97),
              (176, 192, 209)]


# 9 columns x 12 rows

def select_color():
    return random.choice(color_list)


def paint_row(row_position):
    for column in range(int((-canvas_width / 2) + dot_size), int(canvas_width / 2), int(dot_size * 2)):
        tim.setposition(column, row_position)

        tim.dot(dot_size, select_color())


starting_position = (0, 0)
for row in range(int(-canvas_height / 2), int(canvas_height / 2), dot_size * 2):
    paint_row(row)

screen.exitonclick()
