unit=int(input("enter the unit value"))
bill=0
if unit<=100:
    bill=unit*0
elif unit>100 and unit<=200:
    bill=100*0+(unit-100)*5
elif unit>200 and unit<=400:
    bill=100*0+100*5+(unit-200)*10
else:
    bill=100*0+100*5+100*10+(unit-400)*12   
print("total bill=",bill)