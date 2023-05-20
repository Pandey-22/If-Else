p=int(input("enter your 4 digit pin number:"))
print("welcome to state bank of india")
m=25000        
if (p==1234):
    print("1-withdraw")  
    print("2-balance enquiry")  
    print("3-fast cash")   
    c=int(input("please choose transactions:"))            
    if c==1:
        print("invalid cash")            
    elif (c==2):       
        print("your available amount:",m)    
    elif (c==3):   
        print("1.5000")   
        print("2.10000")
        print("3.15000")
        print("4.20000")
    w=int(input("enter withdraw amount:"))      
    if(w<m and w%100==0):            
            print("please take your amount:",w)       
    else:           
       print("4.20000")   
    f=int(input("enter fast cash option:"))
    if (f==1):
            print("please take cash 5000")
    elif (f==2):
            print("please take cash 10000:")
    elif (f==3 ):
            print("please take cash 15000:")
    elif (f==4):
            print("please take cash 20000")
    else:
            print("invalid fast cash option:")
else:
    print("wrong pin")