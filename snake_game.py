from turtle import Screen, Turtle
import time

STARTING_POSITIONS = [(0,0),(20,0),(40,0)]
MOVE_DISTANCE = 20
REFRESH_RATE = 0.3


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_tail = Turtle()
            new_tail.shape("square")
            new_tail.color("white")
            new_tail.penup()
            new_tail.goto(position)
            self.segments.append(new_tail)

    def move(self):
        for segment in range(len(self.segments) - 1, 0, -1):
            coord_x = self.segments[segment - 1].xcor()
            coord_y = self.segments[segment - 1].ycor()
            self.segments[segment].goto(coord_x, coord_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        self.segments[0].setheading(90)

    def down(self):
        self.segments[0].setheading(270)

    def right(self):
        self.segments[0].setheading(0)

    def left(self):
        self.segments[0].setheading(180)


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


# def forward(snake_segments):
#     for segment in snake_segments:
#         segment.forward(20)


# def move(snake_segments):
#     for segment in range(len(snake_segments)-1, 0, -1):
#         coord_x = snake_segments[segment - 1].xcor()
#         coord_y = snake_segments[segment - 1].ycor()
#         snake_segments[segment].goto(coord_x, coord_y)
#     snake_segments[0].forward(20)
#     snake_segments[0].left(90)


snake = Snake()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    snake.move()
    time.sleep(REFRESH_RATE)
    screen.update()
screen.exitonclick()