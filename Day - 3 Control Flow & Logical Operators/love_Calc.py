# This is a simple program that counts the compatibility of 2 people by their names. 
# Here, we are going to use the count() function in python. 

# Here I go. 

print("Welcome to love calculator!")
name1 = input("Enter your name\n")
name1= name1.lower()
name2 = input("Enter your name\n")
name2 = name2.lower()
name = name1 + name2

t = name.count("t")
r = name.count("r")
u = name.count("u")
e = name.count("e")

true = t + r + u + e

l = name.count("l")
o = name.count("o")
v = name.count("v")
e = name.count("e")

love = l + o + v + e

true_love = str(true) + str(love) # Converting the integer data type into string to concatenate the string. 
true_love = int(true_love)

# Now using conditionals, 
if true_love < 10 or true_love > 90:
    print(f"Your score is {true_love}, you go together like coke and mentos.")
elif true_love >= 40 and true_love <= 50:
    print(f"Your score is {true_love}, you are alright together.")
else:
    print(f"Your score is {true_love}.")

