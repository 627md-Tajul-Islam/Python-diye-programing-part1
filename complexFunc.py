def myFunc(x,z,y=10):
    print("x =", x, "y =", y, "z =", z)

myFunc(x=1,y=2,z=5)

a=5
b=6
myFunc(x=a,z=b)

a = 1
b = 2
c = 3
myFunc(y=a,z=b,x=c)