import random
from Art import logo

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm Thinking of number between 1 and 100. ")

number = random.randint(1,101)
print(number)


difficulty = input("Choose a difficulty. Type 'easy' or 'hard'. ").lower()
if difficulty == 'easy':
    life = 10
    print(f"You have {life} attempts remaining to guess the number.")
elif difficulty == 'hard':
    life = 5
    print(f"You have {life} attempts remaining to guess the number. ")


alive = True
while alive:
    guess = int(input("Make a Guess: "))
    if guess > number:
        print("Too high")
        life -= 1
        print(f"You have {life} attempts remaining to guess the number." )
    elif guess < number:
        print("Too Low")
        life -= 1
        print(f"You have {life} attemts remaining to guess the number.")
    elif guess == number:
        print(f"You got it! The answer was {number}.")
        alive = False