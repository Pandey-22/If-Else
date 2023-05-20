a=int(input("enter the 1st number"))
b=int(input("enter the 2nd number"))
c=int(input("enter the 3rd number"))
if a>b and b<c:    
    print("the median number is",a)    
elif b<c and c>a:    
    print("the median number is",b)   
elif c<b and c>a:    
    print("the median number is",c)    
else:    
    print("invailid")