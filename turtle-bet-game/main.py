from turtle import Turtle, Screen
import random


screen = Screen()
screen.setup(width=500, height=400)
is_race_on = False
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["green", "red", "orange", "blue", "purple","pink"]
y_pos = [-100, -50, 0, 50, 100, 150]
all_turtles = []


for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_pos[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

        for turtle in all_turtles:
            if turtle.xcor() > 230:
                is_race_on = False
                winner = turtle.pencolor()
                if winner == user_bet:
                    print(f"You win!! {winner} has won")
                else:
                    print(f"You lost. {winner} has won")

            else:
                rand_distance = random.randint(0, 10)
                turtle.forward(rand_distance)




screen.exitonclick()
