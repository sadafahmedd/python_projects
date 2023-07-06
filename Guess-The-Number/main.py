import random
from art import logo


def game_mode(number):
    attempts = number
    play = True
    while play:
        print(f"you have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if generated_number > guess:
            print("Too Low.")
            if attempts == 1:
                print("Sorry, you have run out of guesses. you lose.")
                play = False
            else:
                print("Guess Again.")
                attempts -= 1

        elif generated_number < guess:
            print("Too High.")
            if attempts == 1:
                print("Sorry, you have run out of guesses. you lose.")
                play = False
            else:
                print("Guess Again.")
                attempts -= 1

        else:
            print(f"You got it the answer was {guess}")
            play = False


print(logo)
print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 - 100.")
generated_number = random.randint(1, 100)

difficulty = input("Choose a difficulty: Type 'easy' or 'hard': ")
if difficulty == "easy":
    game_mode(10)
elif difficulty == "hard":
    game_mode(5)
