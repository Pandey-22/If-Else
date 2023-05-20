num1=int(input("enter the 1st number"))
num2=int(input("enter the 2nd number"))
op=input("enter the operator thease for specific operation")
if op=='+':
    result=num1+num2
    print("Result=",result)
elif op=="-":
    result=num1-num2
    print("Result=",result)
elif op=="*":
    result=num1*num2
    print("Result=",result)
else:
    print("Result is not right")