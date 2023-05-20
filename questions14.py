print("enter a tringle side")
a=int(input("x:-"))
b=int(input("y:-"))
c=int(input("z:-"))
if a==b==c:
    print("equalateral")
elif a==b or b==c or c==a:
    print("isosceles tringle")
else:
    print("scalene tringle")