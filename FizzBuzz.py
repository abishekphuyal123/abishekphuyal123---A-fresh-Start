# The legendary FizzBuzz program - very common interview question. 

for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:       # This is the tricky part, we need to run this line first because if we run %3 == 0 or the %5 == 0 line 1st, we'll either get Fizz or Buzz. 
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    elif i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    else:
        print(i)
        