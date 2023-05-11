#TASK 1
def solution():
    global name
    global price
    name=[]
    price=[]
    total=0
    for i in range (5):
        a=str(input("enter item name:"))
        b=float(input("enter item value"))
        name.append(a)
        price.append(b)
        total= total + b
    return total
output= solution()
for z in range (len (name)):
    print (name[z] , "= ", price[z])

print ("total =",output)
    
