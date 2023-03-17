# Data types exercise: 
# Write a program that adds the digits in a 2 digit number. eg. if the input was 35 the output should be 3 + 5 = 8. 

# first we input a 2 digit number as a string, and convert them into integer and then add the 2 digits to get the result. 

number = input("Enter a 2 digit number: ")
first_digit = int(number[0])
second_digit = int(number[1])
add = first_digit + second_digit
print(f"{first_digit} + {second_digit} = {add}")