def myFunction(x,z,y=10):
    print("x =", x, "y =", y, "z =", z)

myFunction(x = 1,y=2, z=3)
a = 5
b = 6
myFunction(x = a, z =b)
a = 12
b = 13
c = 14
myFunction(y=a,z=b,x=c)