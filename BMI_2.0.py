# Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height. 
# And also returns, if the user is underwright, healthy weight, overweight or clinically obese. 

weight = float(input("Enter your weight. "))
height = float(input("Enter your height. "))
BMI = weight/(height**2)
print(round(BMI,2))
if BMI < 18.5:
    print(f"Your BMI is {BMI}, you are underweight.")
elif BMI > 18.5 and BMI <= 25:
    print(f"Your BMI is {BMI}, you are normal weight.")
elif BMI > 25 and BMI <= 30:
    print(f"Your BMI is {BMI}, you are slightly overweight. ")
elif BMI > 30 and BMI <= 35:
    print(f"Your BMI is {BMI}, you are obese.")
elif BMI > 35:
    print(f"Your BMI is {BMI}, you are clinically obese.")

# This program asks for the weight and height of the user, and calculates the BMI of the user. 
# And displays whether the user is healthy weight, over weight, obese or clinically obese, using the if & elif statements. 