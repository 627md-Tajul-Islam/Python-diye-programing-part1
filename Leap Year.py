
#Method 1
year = input("Enter year :")
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

print("Program Terminated")
#Method 2
year = input("Enter Year :")
year = int(year)

if year % 4 !=0:
    print("No")
else:
    if year % 100 !=0:
        print("yes")
    else:
        if year%400 !=0:
            print("No")
        else:
            print("Yes")

print("Program Terminated")

#Method 3
year = input("Enter Year :")
year = int(year)

if year% 400 == 0:
    print("Yes")
elif year%100 == 0:
    print("No")
elif year%4 == 0:
    print("Yes")
else:
    print("No")

#Method 4
year = input("Enter Year :")
year = int(year)

if year % 100 !=0 and year%4==0:
    print("yes")
elif year%100 == 0 and year%400 ==0:
    print("yes")
else:
    print("No")