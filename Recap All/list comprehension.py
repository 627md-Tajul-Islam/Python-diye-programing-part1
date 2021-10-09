# normal way
list = [1,2,3,4]
newLi = []
for x in list:
    newLi.append(2 * x)
print(newLi)

# list comprehesion
li = [1,2,3,4]
newLi = [2 * x for x in li]
print(newLi)