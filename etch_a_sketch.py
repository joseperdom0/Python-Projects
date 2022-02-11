from turtle import Turtle, Screen

t = Turtle()
screen = Screen()


def move_forwards():
    t.forward(distance_walked)


def move_backwards():
    t.backward(distance_walked)


def rotate_clockwise():
    t.right(angle_moved)


def rotate_counter():
    t.left(angle_moved)


def clear_screen():
    t.goto(0, 0)
    t.clear()


screen.listen()
distance_walked = 15
angle_moved = 10
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="d", fun=rotate_clockwise)
screen.onkey(key="a", fun=rotate_counter)
screen.onkey(key="c", fun=clear_screen)

screen.exitonclick()
