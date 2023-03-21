import random

Rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

Paper = """
    _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

Scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
images = [Rock, Paper, Scissors]
human = int(input("What do you choose? Enter 0 for Rock, 1 for Paper & 2 for Scissors."))
if human >2 or human<0:
    print("Invalid Input, you lose.🥶")
else:
    print("Human Chose: 👦")
    print(images[human])

    computer_choice = random.randint(0,2)
    print("Computer Chose: 🤖")
    print(images[computer_choice])

    if computer_choice == 0 and human == 2:
        print("You Lose! 😨")
    elif human == 0 and computer_choice == 2:
        print("You Win. 😁")
    elif human > computer_choice:
        print("You Win 😁")
    elif computer_choice > human:
        print("You Lose 😨")

