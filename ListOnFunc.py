'''
def add_numbers(numbers):
    result = 0
    for number in numbers:
        result = result + number
    return result

result = add_numbers([1,2,30,4,5,9])
print(result)
'''
"""
def add_numbers(numbers):
    result = 0
    for number in numbers:
        result = result + 1
    return result

result = add_numbers([1,2,30,4,50])
print(result)

def test(li):
    li[0] = 10

my_list = [1,2,3,4,5]
print("Before Function Call", my_list)
test(my_list)
print("After Function Call", my_list)
"""

list1 = [1,2,3,4]
list2 = list1
print(list1)
print(list2)

list2[0] = 100
print(list2)
print(list1)