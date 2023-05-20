unit=int(input("enter the unit value"))
if (unit<=200):
    bill=unit*6
elif (unit>200 and unit<=400):
    bill=unit*6+(unit-200)*8
elif (unit>400 and unit<=600):
    bill=200*6+200*7+(unit-400)*8
else:
    bill=200*6+200*7+200*8+(unit-600)*10
print("total bill:",bill)