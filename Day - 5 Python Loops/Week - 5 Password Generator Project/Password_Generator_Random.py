import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0','1','2','3','4','5','6','7','8','9']

symbols = ['+','#', '(', ')', '!', '*', '£', '$', '%', '&']

print("Welcome to Abishek's Password Generator: ")

n_letters = int(input("Enter the number of letters you want in your password. \n"))
n_numbers = int(input("Enter the number of numbers you want in your password. \n"))
n_symbols = int(input("Enter the number of symbols you want in your password. \n"))

# First, we are going to use the for loops and the choice function to create the different sections of the password. 

password = " "

for i in range(1,n_letters+1):
    password += random.choice(letters)

for j in range(1,n_numbers + 1):
    password += random.choice(numbers)

for k in range(1, n_symbols + 1):
    password += random.choice(symbols)

print(password) 
# # As this is the password that is generated and is quite easy for professional hackers to guess, now we have to shuffle it and make it unpredictable. 
# Here's I am using my own twist to rearrange the string password. 

password = list(password) # First Convert it into a list. 

random.shuffle(password) # Then using the python shuffle() funtion, which shuffles the contents inside a mutable sequence such as list, as a string is an immutable sequence, we cannot use the shuffle function. 

new_password = ''.join(password) # As, the password is converted into a list, we use the join function to convert it into a string. 
print(new_password)
