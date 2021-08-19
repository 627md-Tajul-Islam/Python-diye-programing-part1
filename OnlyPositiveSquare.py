while True:
    n = input("Please Enter a Positive Number (Do not input 0) : ")
    n = int(n)
    if n < 0:
        print("Only positive numbers allowed.Try Again")
        continue
    if n == 0:
        break
print("Square of", n, "is", n*n)