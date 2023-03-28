# This is a simple program to calculate the BMI based on user's weight and height. 
# The method to calculate BMI is: Weight / (height^2)

# As weight and height could be floating values, we enter the values as float. 
weight = float(input("Enter your weight in kg. "))
height = float(input("Enter your height in m. "))
BMI = weight / (height ** 2) 
# Here, we round the BMI to the nearest whole number using the round function. 
BMI = round(BMI)
print(f"Your BMI is {BMI}.")
