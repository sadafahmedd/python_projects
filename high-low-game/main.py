import random
from art import logo
from art import vs
from game_data import data


print(logo)
score = 0
play = True
b = random.choice(data)
while play:
    a = b
    name = a["name"]
    followers1 = a["follower_count"]
    description = a["description"]
    country = a["country"]

    print(f"Compare A: {name}, a {description} from {country}")

    print(vs)
    # Second choice
    b = random.choice(data)
    name = b["name"]
    followers2 = b["follower_count"]
    description = b["description"]
    country = b["country"]

    print(f"Against B: {name}, a {description} from {country}")

    answer = input("Who has more followers? Type A or B: ").lower()

    if answer == "a":
        if followers1 > followers2:
            score += 1
            print(f"Youre Right, Current score: {score}")

        else:

            print(f"Youre Wrong, Final score: {score}")
            play = False

    elif answer == "b":
        if followers1 < followers2:
            score += 1

            print(f"Youre Right, Current score: {score}")

        else:

            print(f"Youre Wrong, Final score: {score}")
            play = False

