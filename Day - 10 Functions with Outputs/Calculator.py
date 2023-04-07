from logo import logo  


# Here, first of all we create functions of the different mathematical operations. 
# This is a simple calculator program created with the help of python functions. 
# It combines 4 different functions, the add(), sub(), mul() & the div() functions to create a simple calculator and introduces recursion to the learning path. 


# The Addition Function. 
def add(n1,n2):
  """Takes 2 numbers and returns the addition of them."""
  return n1 + n2

# The Subtraction Function.
def sub(n1,n2):
  """Takes 2 numbers and returns their difference."""
  return n1 - n2

# The Multiplication Function.
def mul(n1,n2):
  """Takes 2 numbers and returns their product."""
  return n1 * n2

# The division function. 
def div(n1,n2):
  """Takes 2 numbers as inputs and returns their division."""
  return n1/n2

operations = { # Storing the different operations inside a dictionary. 
  "+" : add,
  "-" : sub,
  "*" : mul,
  "/" : div,
}
def calculator(): 
  print(logo) # Printing the ascii art, imported from the file logo.py
  num1 = float(input("\nWhat is the first number: \n"))
  for keys in operations: # looping through the dictionary operations to print out the elements inside the list. 
    print(f"\n {keys}")
  should_continue = True
  
  while should_continue:    # Starting of the while loop
    operation_symbol = input("\nPick an operation: ")
    num2 = float(input("\nWhat is the second number: "))
    calculation_function = operations[operation_symbol] 
    answer = calculation_function(num1,num2)
  
    print(f"Your total is {num1} {operation_symbol} {num2} = {answer}")
  
    if input(f"Type 'y' to continue or type 'n' to start new calculation: ") == "y":
      num1 = answer
    else:
      should_continue = False
      calculator()

calculator()
  
  
   
    