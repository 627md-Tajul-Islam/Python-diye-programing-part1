def myFunction(x):
    print("This is from inside", x)
    x = 10
    print("This is also from inside", x)

x = 100
myFunction(x)
print("this is from outside", x)