
A = True
while A == True:
    n = int(input("Enter number of rows: "))
    i = int(1)
    while n != 0:
        print("* "*i, "\n")
        i += 2
        n -= 1
    A = input("Do you want to run the program again? (y/n): ")
    if A == "y":
        A = bool(1)
    else:
        A = bool(0)
