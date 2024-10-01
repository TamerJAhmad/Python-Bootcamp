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

choice_list = [rock, paper, scissors]

print("\nHello! Welcome to Tamer's Rock, Paper, Scissors Game!"
      "\n\nThe rules are simple: "
      "\n\tRock beats Scissors\n\tPaper beats Rock\n\tand Scissors beats Paper!\n")

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

computer_choice = random.randint(0, int(len(choice_list) -1))

print("You choose: " + choice_list[int(user_choice)])
print("Computer chose: " + choice_list[computer_choice])

if user_choice == computer_choice:
    print("It's a tie! You both are Winners!")
elif user_choice == 0 and computer_choice == 1:
    print("Oh no! Computer Wins, better luck next time.")
elif user_choice == 0 and computer_choice == 2:
    print("Rock beats Scissors! You Win!")
elif user_choice == 1 and computer_choice == 0:
    print("Paper beats Rock! You Win!")
elif user_choice == 1 and computer_choice == 2:
    print("Oh no! Computer Wins, better luck next time.")
elif user_choice == 2 and computer_choice == 0:
    print("Oh no! Computer Wins, better luck next time.")
elif user_choice == 2 and computer_choice == 1:
    print("Scissors beats Paper! You Win!")
else:
    print("Sorry that's not a valid input. Try Again.")
