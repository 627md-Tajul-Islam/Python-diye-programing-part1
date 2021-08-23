"""
def myFunc(x):
    print("Inside myFunction",x)
    x = 10
    print("Inside myFunction",x)

x = 20
myFunc(x)
print(x)


def myFunction(y):
    print("y =",y)
    print("x =",x)

x = 30
myFunction(x)


def myFunction(y=10):
    print("y =",y)

x = 20
myFunction(x)
myFunction()
 """
""" 
def myFunction(x, y=10, z=3):
    print("x =", x,"y =", y,"z =", z)

x = 5
y = 6
z = 7

myFunction(x,y,z)
myFunction(x,y)
myFunction(x)
"""

def myfunc(x,z,y=10):
    print("x =", x, "y =", y, "z =", z)

myfunc(x = 1, y = 2, z = 5)
a = 5
b = 6
myfunc(x = a, z = b)
a = 1
b = 2
c = 3
myfunc(y=a,z=b,x=c)



def myFunc(x,y=10,z=0):
    print("x =", x, "y =", y, "z =", z)

x = 5
y = 6
z = 7

myFunc(x,y,z)
myFunc(x)
myFunc(y)
myFunc(z)
myFunc(x,y)
myFunc(x,z)
myFunc(x,z)