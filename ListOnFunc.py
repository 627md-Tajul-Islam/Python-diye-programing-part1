'''
def add_numbers(numbers):
    result = 0
    for number in numbers:
        result = result + number
    return result

result = add_numbers([1,2,30,4,5,9])
print(result)
'''

def test_fnc(li):
    li[0] = 10

list = [1,2,3,4]
print("Before FUnction Call", list)
test_fnc(list)