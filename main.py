from turtle import Turtle, Screen
import random

screen = Screen()

#Resizing the screen
screen.setup(width=500,height=400)

#popup asking user for bet
user_bet = screen.textinput(title="make your bet", prompt="What color turtle do you bet will win?")

is_race_on = False
colors = ["red", "orange", "yellow","green","blue", "purple"]
y_position = -70
all_turtles = []

for x in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[x])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_position)
    y_position = y_position + 30
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                screen.textinput(title="You Win!", prompt=f"The {winning_color} turtle is the winner")
            else:
                screen.textinput(title="You Lose!", prompt=f"The {winning_color} turtle is the winner")
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)






screen.exitonclick()