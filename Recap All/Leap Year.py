year = int(input("Enter a year: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(year, "is a leap year")
else:
    print("THis is not a leap year")

print("End")

# 2nd way

if year % 100 != 0 and year % 4 == 0:
