# This program takes a year as an input, and outputs whether the given year is a leap year or not. 
year = int(input("Enter a year. "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"Yes, the year {year} is a leap year.")
        else:
            print(f"No, the year {year}, is not a leap year")
    else:
        print(f"Yes, the year {year}, is a leap year")
else:
    print(f"No, the year {year} is not a leap year.")        
    