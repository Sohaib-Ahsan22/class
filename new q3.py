print("Question:3")
num=int(input("enter any integer"))
print("following are the devisor of",num)
for i in reversed(range(1,num+1)):
    if num%i==0:
        print(i)
