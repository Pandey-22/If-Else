costprice=int(input("enter price of bike"))
if costprice>100000:   
    tax=costprice*15/100  
    print("the road tax is",tax)   
elif costprice>=10000 and costprice<=100000: 
    tax=costprice*10/100   
    print("the road tax is",tax)     
else:  
    print("tax free")