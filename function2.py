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

def myFunction(x, y=10, z=3):
    print("x =", x,"y =", y,"z =", z)

x = 5
y = 6
z = 7


myFunction(x,y,z)
myFunction(x,y)
myFunction(x)