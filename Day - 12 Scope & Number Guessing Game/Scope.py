# Here, we are going to talk about the scope in python. 1. Global vs 2. Local Scope. 

# Example of Local and Global Scope. 

enemies = 1 

def increase_enemies():
    enemies = 2
    print(f"The number of enemies: {enemies}.")

increase_enemies() # Once we call the function we, get the output - 2. This is a local variable that can be only used inside the function 'increase_enemies()'. 

print(f"The number of enemies: {enemies}.") # From this print statement, we get the output, 1, as this is declared outside a function thus, it is a global variable. 

