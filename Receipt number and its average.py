# Receipt Program
s=0
x=0
amt=0
while amt>=0:
    amt=float(input("Enter the receipt number:"))
    if amt>=0:
        s=s+amt
        x=x+1
avg=s/x
print("Total Receipt Number=%.f,Total Average:%.f"%(s,avg))
