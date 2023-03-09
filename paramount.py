size = 5
for i in range(size):
    for j in range(1, size - i):
        print(" ", end="")
    for k in range(2*i-1):
        print("*", end="")
    print()
