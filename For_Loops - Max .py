number = input("Enter a few numbers separated by space. ").split()
for n in range(0,len(number)):
    number[n] = int(number[n])

max = 0
for i in number:
    if i > max:
        max = i
print(f"The maximum number is: {max}")
