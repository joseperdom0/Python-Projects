import random
from turtle import Screen, Turtle
import time

STARTING_POSITIONS = [(0,0),(20,0),(40,0)]
MOVE_DISTANCE = 20
REFRESH_RATE = 0.05
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
FONT = ("Courier", 24, "normal")

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

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
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.speed("fastest")
        self.color("white")

    def spawn(self):
        random_x = random.randint(-280,280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.display_score()

    def display_score(self):
        self.clear()
        self.goto(0, 260)
        self.color("white")
        self.hideturtle()
        self.write(f"Score = {self.score}", False, align="center", font = FONT)

    def increase_score(self):
        self.score += 1
        self.display_score()

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write("GAME OVER", False, align="center", font= FONT)


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
food = Food()
scoreboard = Scoreboard()

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
    if snake.head.distance(food) < 15:
        scoreboard.increase_score()
        print(scoreboard.score)
        food.spawn()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()
screen.exitonclick()