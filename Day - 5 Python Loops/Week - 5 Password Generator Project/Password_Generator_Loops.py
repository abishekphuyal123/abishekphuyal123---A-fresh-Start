import random 

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0','1','2','3','4','5','6','7','8','9']

symbols = ['+','#', '(', ')', '!', '*', '£', '$', '%', '&']

print("Welcome to Abishek's Password Generator: ")

n_letters = int(input("Enter the number of letters you want in your password. \n"))
n_numbers = int(input("Enter the number of numbers you want in your password. \n"))
n_symbols = int(input("Enter the number of symbols you want in your password. \n"))

password = ""

for i in range(1,n_letters + 1): # For letters
    password += random.choice(letters)

for j in range(1, n_numbers + 1):
    password += random.choice(numbers)

for k in  range(1,n_symbols + 1):
    password += random.choice(symbols)

print(password) 



# This is another way of Generating Passwords in python by utilizing the for loops and the random() module - and the choice () function from the random() module. 
# As we can see that the sequence of the passwords generated from this program is quite predictable, as the password 1st consists of letters, numbers and then the symbols. 

# Now, in the next step, we are going to create a password generator that is completely unpredictable. 
