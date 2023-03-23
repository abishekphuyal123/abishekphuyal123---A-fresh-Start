import random 

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0','1','2','3','4','5','6','7','8','9']

symbols = ['+','#', '(', ')', '!', '*', '£', '$', '%', '&']

print("Welcome to Abishek's Password Generator: ")

n_letters = int(input("Enter the number of letters you want in your password. \n"))
n_numbers = int(input("Enter the number of numbers you want in your password. \n"))
n_symbols = int(input("Enter the number of symbols you want in your password. \n"))

i = random.sample(letters, n_letters)

j = random.sample(numbers, n_numbers)

k = random.sample(symbols, n_symbols)

add = i + j + k
password = ''.join(add)

print(f"You'r password is: {password}.")

# This is a password generator program without using for loops. 
# We are going to create 3 different versions of this program. 