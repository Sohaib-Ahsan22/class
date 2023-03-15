x = int(input("enter max number of rows:"))
y= x+1
for i in range(y):
    for j in range(1, y - i):
        print(" ", end="")
    for k in range(2*i-1):
        print("*", end="")
    print()

