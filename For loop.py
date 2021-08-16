#for i in range(5):
   # print("I love ALLAH")

import turtle
turtle.shape("turtle")
turtle.speed(1)

for i in range(4):
    turtle.forward(100)
    turtle.left(90)
turtle.exitonclick()

result = 0
for i in range(5):
    result = result + 1
    print(result)



result = 0
num = 1
for _ in range(50):
    result = result + num
print(result)


result = 0
for num in range(51):
    result = result + num

print(result)



result = 0
for num in range(1,51):
    result = result + num
print(result)


for i in range (1,20,5):
    print(i)

for i in range(1,20,1):
    print(i)


numbers = [1123,13234,35463,2342342,6543634563453]
max_num = numbers[0]
for num in numbers:
    if num > max_num:
        max_num = num
print(max_num)

result = 0
for num in range(101):
    if num % 5 ==0:
        print(num)
        result =  result + num
print("Total Sum Is :", result)

result = 0
for num in range(5,101,5):
    print(num)
    result = result + num
print("Sum is: ", result)