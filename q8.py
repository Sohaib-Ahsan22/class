print("Question number 8")
import math
a=float(input("length of 1st side:"))
b=float(input("length of 2nd side:"))
c=float(input("length of 3rd side:"))
s=(a+b+c)/2
ans=math.sqrt(s*((s-a)*(s-b)*(s-c)))
print("The area of tha triangle is=%.2f"%(ans))
