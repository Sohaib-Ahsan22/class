#TASK 4
def password_cal():
    password=input("Enter the password:")
    special_char=['!' ,'@',' #',' $','%','^','&']
    has_lowercase= False
    has_uppercase= False
    has_special= False
    if len(password)>=8:
        for i in password:
            if ord(i)>=97 and ord(i)<=122:
                has_lowercase= True
            elif ord(i)>=65 and ord(i)<=90:
                has_uppercase= True     
            elif i in special_char:
                has_special= True
        if has_lowercase==True and has_uppercase==True and has_special==True:
            print("Password is valid/ok/strong!!")

        if not has_lowercase:
            print("Password must atleast have one lowercase!!")
        if not has_uppercase:
            print("Password must atleast have one uppercase!!")
        if not has_special:
            print("Password must atleast have one special character!!")
    else:
        print("Password not valid! Must be 8 characters!!")

password_cal()
        
