num1=int(input("Enter first number"))
num2=int(input("Enter second number"))
num3=int(input("Enter third number"))
if num1>num2 and num1>num3:
      if num2>num3:
            print("The second largest number is",num2)
      else:
            print("The largest number is",num3)
elif num2>num1 and num2>num3:
      if num1>num3:
            print("The second largest number is", num1)
      else:
            print("The second largest number is", num3)
else:
      if num1>num2:  
        print("The second largest number is",num1)
      else:
        print("The second largest number is", num2)