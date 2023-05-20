quantity=int(input("enter the value of required quantity"))
cost=100
totalcost=quantity*cost
if totalcost>1000:
    print("your total cost is {} with 10% discount",format(totalcost))
else:
    print("your total cost is",totalcost)