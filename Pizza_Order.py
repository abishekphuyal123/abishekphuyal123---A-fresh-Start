# Build an automatic pizza order program. 
"""
Based on the user's order, work out their final bill. 
small Pizza : $15
Medium Pizza : $20
Large Pizza : $25. 
Pepperoni for small pizza: +$2
Pepperoni for Medium&Large pizza: +$3
Extra charge for any size pizza: +$1.
"""

# Here's the code for the program. 
print("Welcome to pepe's pizza.")
size = input("What size pizza would you like? 'S', 'M', 'L'")
size = size.lower()
pepperoni = "Would you like to add pepperoni to your pizza? 'Y' or 'N'"
pepperoni = pepperoni.lower()
cheese = "Would you like extra cheese on your pizza? 'Y' or 'N'."
cheese = cheese.lower()
total_amount = 0

# We will be using highly nested if statements for this project. 
if size =="s":
    total_amount+=15
    topping = input(pepperoni)
    if topping =="y":
        total_amount+=2
        extras=input(cheese)
        if extras=="y":
            total_amount+=1
        elif extras=="n":
            total_amount+=0
        else:
            print("Invalid Input")
    elif topping =="n":
        total_amount+=0
        extras=input(cheese)
        if extras=="y":
            total_amount+=1
        elif extras=="n":
            total_amount+=0
        else:
            print("Invalid Input")
    else:
        print("Invalid Input")

elif size =="m":
    total_amount+=20
    topping=input(pepperoni)
    if topping=="y":
        total_amount+=3
        extras = input(cheese)
        if extras=="y":
            total_amount+=1
        elif extras=="n":
            total_amount+=0
        else:
            print("Invalid Input")
    elif topping=="n":
        total_amount+=0
        extras = input(cheese)
        if extras=="y":
            total_amount+=1
        elif extras=="n":
            total_amount+=0
        else:
            print("Invalid Input")
    else:
        print("Invalid Input")


elif size =="l":
    total_amount+=25
    topping=input(pepperoni)
    if topping=="y":
        total_amount+=3
        extras=input(cheese)
        if extras=="y":
            total_amount+=1
        elif extras =="n":
            total_amount+=0
        else:
            print("Invalid Input")
    elif topping =="n":
        total_amount+=0
        extras=input(cheese)
        if extras =="y":
            total_amount+=1
        elif extras=="n":
            total_amount+=0
        else:
            print("Invalid Input")
    else:
        print("Invalid Input")
print(f"\n\tYour order total is {total_amount}")

    
    


    
