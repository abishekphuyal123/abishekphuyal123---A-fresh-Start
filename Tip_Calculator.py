# This is a simple calculator program that divides the total bill by the number of people and add the tip. 
# Let's see the program running. 

people = input("Enter total number of people: ")
bill = input("Enter the total amount. ")
people = float(people)
bill = float(bill)
tip = float(input("Enter the tip amount"))
tip /= 10
amount_to_split = (bill/people)*tip
amount_to_split = round(amount_to_split,2)
print(f"Each person has to pay {amount_to_split}. ")

