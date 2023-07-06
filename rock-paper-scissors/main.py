import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇
# what user chooses

choice = int(input("What do you want to choose? Type 0 for Rock, Type 1 for Paper, Type 2 for Scissors: "))
print("You chose: ")
if choice == 0:
    human = "rock"
    print(rock)
elif choice == 1:
    human = "paper"
    print(paper)
else:
    human = "scissors"
    print(scissors)

# what computer chooses
print("Computer chose: ")
options = [rock, paper, scissors]
a = len(options)
b = random.randint(0, a - 1)
print(options[b])

if options[b] == rock:
    computer = "rock"
elif options[b] == paper:
    computer = "paper"
else:
    computer = "scissors"

# who wins
if human == "rock" and computer == "rock":
    print("TIE")
elif human == "rock" and computer == "paper":
    print("YOU LOSE")
elif human == "rock" and computer == "scissors":
    print("YOU WIN")
elif human == "paper" and computer == "rock":
    print("YOU WIN")
elif human == "paper" and computer == "paper":
    print("TIE")
elif human == "paper" and computer == "scissors":
    print("YOU LOSE")
elif human == "scissors" and computer == "rock":
    print("YOU LOSE")
elif human == "scissors" and computer == "paper":
    print("YOU WIN")
else:
    print("TIE")

