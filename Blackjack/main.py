# Dealing the cards
import random
from replit import clear


def deal_card():
    """Returns random card from deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def calculate_score(list):
    if sum(list) == 21 and len(list) == 2:
        return 0

    if 11 in list and sum(list) > 21:
        list.remove(11)
        return list.append(1)

    return sum(list)


def compare(user_score, computer_score):
    if computer_score == user_score:
        return "Draw 🙃"
    elif computer_score == 0:
        return "You Lost 😢"
    elif user_score == 0:
        return "You Won 🥳"
    elif user_score > 21:
        return "You Lost 😢"
    elif computer_score > 21:
        return "You Win 🥳"
    elif computer_score > user_score:
        return "You Lost 😢"
    else:
        return "You Won 🥳"


from art import logo

start = True
while start == True:
    user_cards = []
    computer_cards = []

    print(logo)
    is_game_over = False
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while is_game_over == False:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards : {user_cards},  Current Score : {user_score}")
        print(f"Computer's first card : {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True

        else:
            question = input("Do you want to draw another card ? y or n: ")
            if question == "y":
                user_cards.append(deal_card())
            elif question == "n":
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand is : {user_cards} and Final score : {user_score}")
    print(f"Computer final hand is : {computer_cards} and Final score is : {computer_score}")
    print(compare(user_score, computer_score))
    question = input("Do you wanna restart? y or n: ")
    if question == "y":
        clear()
    else:
        start = False

