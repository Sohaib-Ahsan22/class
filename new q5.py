print("Question:05")
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
if num1>num2:
    for i in range (1,num1+1):
        if num1%i==0 and num2%i==0:
            print (i)
elif num1<num2:
    for i in range (1,num2+1):
        if num1%i==0 and num2%i==0:
            print (i)
    
