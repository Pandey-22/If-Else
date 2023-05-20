salary=int(input("enter your salary"))
service=int(input("how many years of your service in our company"))
if service>5:
    bonus=0.05*salary
    print("your net bonous amount is",bonus)
else:
    print("your bonous cannot be generated duo to your service is not more than 5 years")