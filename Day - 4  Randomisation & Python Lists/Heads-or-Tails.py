# This is a simple coin toss program using the random module in python. 
# First we import the random module. 

import random
number = random.randint(0,1) # We are creating either 0 or 1, random number. 
if number == 0:
    print("Tails")
else:
    print("Heads")
