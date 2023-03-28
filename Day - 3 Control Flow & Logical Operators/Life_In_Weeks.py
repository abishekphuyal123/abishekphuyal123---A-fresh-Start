"""Create a program using maths and f-strings, that tells us how many days, months, weeks, we have left if 
we live until the age of 90 years. """
# A year has 365 Days, 52 Weeks & 12 Months.
age= int(input("Enter your age. "))
months = (90-age) * 12
weeks = (90 - age)*52
Days = (90 - age)*365
print(f"You have {months} months, {weeks} weeks, and {Days} days to live in this world.")
print("Hello World.")