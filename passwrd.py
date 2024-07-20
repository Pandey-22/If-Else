password=input("enter the password")
if len(password)>=1 and len(password)<=9:
    if "@" in password or "$" in password or "#" in password:
        if "A" or "Z" in password:
            if "a" or "z" in password:
                print("strong password")
            else:
                print("no strong password")
        else:
            print("wrong password")
    else:
        print("enter the special character")
else:
    print("enter new password")