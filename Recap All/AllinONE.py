kill = False
while not kill:
    num1 = int(input("Enter 1st Number: "))
    num2 = int(input("Enter 2nd Number: "))

    while True:
        action = input("Please enter add/sub/multiply/division (quit to exit):  ")
        if action == "quit":
            kill = True
            break
        if action not in ["add","sub","multiple","division"]:
            print("Action Unknown !")
        if action == "add":
            print("Sum of 2 numbers is:", num1 + num2)
            break
        if action == "sub":
            print("Subtraction of 2 numbers is ", num1 - num2)

