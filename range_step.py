# Here, we are going to print the sum of only even numbers from 1 to 100. 
# We'll use the range() function including the step value for the range.

sum = 0
for i in range(2,101,2):
    sum += i
print(f"The sum of even numbers from 1 to 100 is: {sum}")