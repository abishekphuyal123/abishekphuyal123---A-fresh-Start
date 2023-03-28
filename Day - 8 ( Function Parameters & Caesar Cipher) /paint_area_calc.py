import math

def print_calc(test_h, test_w, cover):
    total = (test_h * test_w) / cover
    total = math.ceil(total)    
    print(f"Therefore, the total cans of paint needed is: {total}. ")

height = int(input("Enter the wall height: \n"))
width = int(input("Enter the wall width: \n"))
coverage = 5
print_calc(test_h=height, test_w=width, cover=coverage)
