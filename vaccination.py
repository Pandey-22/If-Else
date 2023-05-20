n=int(input("enter your current age"))
vaccination=int(input("enter the number"))
if n>=18:
    if vaccination==1:
        print("first dose")
    elif vaccination==2:
        print("second dose")
    elif vaccination==3:
        print("third dose")
else:
    print("you never got vaccinated")