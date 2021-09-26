def myFunction(x):
    print("This is from inside", x)
    x = 10
    print("This is also from inside", x)

y = 100
myFunction(y)
print("this is from outside", y)