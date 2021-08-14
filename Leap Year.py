year = input("Enter year")
year = int(year)
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("yes")
        else:
            print("No")
    else:
        print("yes")
else:
    print("No")