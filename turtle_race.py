from turtle import Turtle, Screen
import random

screen = Screen()

screen_width = 500
screen_height = 400
screen.setup(width=screen_width, height=screen_height)
user_bet = screen.textinput(title="Make your Bet", prompt="Which turtle will win the race? Enter a color:")
colors = ["red", "blue", "purple", "yellow", "orange", "black"]
number_of_turtles = 6


def turtle_creation():
    turtles = []
    for turtle_i in range(6):
        new_turtle = Turtle()
        new_turtle.penup()
        new_turtle.shape("turtle")
        new_turtle.color(colors[turtle_i])
        turtles.append(new_turtle)
    return turtles


def turtle_position(turtles):
    x_pos = -screen_width / 2 + 20
    y_pos = -screen_height / 2 + 80
    for turtle_i in turtles:
        turtle_i.goto(x_pos, y_pos)
        y_pos += 40
    return True


def advance_turtles(turtles):
    racing = True
    winner = ""
    while racing:
        for turtle_i in turtles:
            if turtle_i.xcor() < screen_width / 2 - 20:
                turtle_i.forward(random.randint(0, 10))
            else:
                winner = colors[turtles.index(turtle_i)]
                racing = False
                if winner == user_bet:
                    print("You won!")
                else:
                    print("You lost!")
    print(f"winner is {winner} ")
    return False


is_race_on = False
racing_turtles = turtle_creation()
is_race_on = turtle_position(racing_turtles)

while is_race_on:
    is_race_on = advance_turtles(racing_turtles)

screen.exitonclick()
