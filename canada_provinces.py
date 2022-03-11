import turtle
screen = turtle.Screen()
screen.title("Canada Provinces")
image = "canada_map.gif"
screen.addshape(image)
turtle.shape(image)

answer_province = screen.textinput(title="Guess the Province",prompt="Type the Province name:")
 