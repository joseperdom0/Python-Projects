from turtle import Screen, Turtle
screen = Screen()

class Paddle(Turtle):
    # width 20, height 100, xpos 350, ypos 0
    def __init__(self):
        super.__init__()




screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("PONG!")
screen.exitonclick()