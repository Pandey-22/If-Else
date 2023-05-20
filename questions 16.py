p=int(input("enter marks for physics"))
ch=int(input("enter marks for chemistry"))
b=int(input("enter marks for biology"))
m=int(input("enter marks for mathematic"))  
c=int(input("enter marks for computer"))
tot=p+ch+b+m+c
per=tot/5
if per>90: 
    grade='A'  
elif per>80 and per<=90:  
    grade='B'   
elif per>70 and per<=80:    
    grade='C'    
elif per>60 and per<=70:    
    grade='D'    
elif per>50 and per<=60:    
    grade='E'        
elif per>40 and per<=50:    
    grade='F'        
else:    
    grade="reappear"     
print("total marks:",tot)
print("percentage:",per)
print("grade:",grade)