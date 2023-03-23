# Building a simple program that takes in string separated by spaces as height of people and converts them into integers and returns the average of the given numbers. 

height = input("Enter height separated by spaces. ").split()

for n in range(0,len(height)):
    height[n] = int(height[n])

sum = 0 

for i in height:
    sum += i

print(round(sum/len(height)))

# 156 178 165 171 187