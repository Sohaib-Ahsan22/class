#TASK 2
def weather():
    celsius=float(input("enter temp in celsius:"))
    fahrenheit=(celsius*(9/5))+32
    a=fahrenheit
    if a <= 32:
        print ("temperature is very cold")
    elif a>32 and a<=59:
        print("temperature is cold")
    elif a>59 and a<= 65:
        print("temperature is warm")
    elif a>65 :
        print("temperature is hot")
weather()
    
