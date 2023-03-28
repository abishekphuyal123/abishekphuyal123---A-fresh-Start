# This program takes a string as an input, and separates the string into a list using the split() function, separated by commas.
# It stores the string into a list, and prints out random names from the given list, to show who will pay the bill. 

# Here I go: 

import random
print("Let's find out who's going to pay the bill!!")
string = input("Enter names separated by comma and space: ")
names = string.split(", ") # We split the above entered string into list, using the split() function and split when we see a ", " i.e comma & space.
length = len(names)

random_number = random.randint(0, length-1) # We subtract the length by 1 because the index starts from 0 in the list. 
person = names[random_number]
print(f"{person} is going to pay the bill today.") # Using f-string literal

