while True:
    n = input("Enter a number (Do not use 0): ")
    n = int(n)
    if n == 0:
        break
    print("Square of", n, "is", n*n)