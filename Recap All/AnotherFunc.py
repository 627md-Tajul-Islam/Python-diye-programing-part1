def myFunction(x):
    print("This is from inside", x)
    x = 10
    print("This is also from inside", x)

y = 20
myFunction(y)
print(y)