a=int(input("enter the 1st number"))
b=int(input("enter the 2nd number"))
c=int(input("enter the 3rd number"))
if a>b and a>c and c<a and c<b:
    print("Max number=",a,"Min number=",c)
elif b>a and b>c and c<a and c<b:
    print("Max number=",b,"Min number=",c)
elif c>a and c>b and a<b and a<c:
    print("Max number=",c,"Min number=",a)
elif c>a and c>b and b<a and b<c:
    print("Max number=",c,"Min number=",b)
else:
    print("All numbers are same")
    
# a=int(input("enter the 1st number"))
# b=int(input("enter the 2nd number"))
# c=int(input("enter the 3rd number"))
# if a>b and b<c:    
#     print("the median number is",a)    
# elif b<c and c>a:    
#     print("the median number is",b)   
# elif c<b and c>a:    
#     print("the median number is",c)    
# else:    
#     print("invailid")

