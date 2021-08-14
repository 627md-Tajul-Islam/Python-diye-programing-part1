
n1 = 30
n2 = 40
n3 = 10

if n1 > n2 and n1 > n3:
    print("Max Number: ", n1)

elif n2 > n1 and n2 > n3:
     print("Max Number: ", n2)

else:
     print("Max Number: ", n3)


# another method
num1 = 60
num2 = 70
num3 = 80

if num1 > num2:
    max = num1
else:
    max = num2
if num3 > max:
    max = num3
print("Max : ", max)