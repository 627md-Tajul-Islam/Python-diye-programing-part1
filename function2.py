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
 """

def myFunction(y=10):
    print("y =",y)

x = 20
myFunction(x)
myFunction()