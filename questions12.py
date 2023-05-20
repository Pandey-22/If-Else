notes=[2000,500,200,100,50,20,10,5,2]
amount=int(input("enter the amount"))
for i in range(8):
    print("Rs.",notes[i],"notes will be amount/notes[i]")
    amount=amount%notes[i]





q=int(input("enter a lenth of side 1:-"))
p=int(input("enter a lenth of side 2:-"))
r=int(input("enter a lenth of side 3:-"))
if p+q<r or q+r<p or p+r<q:
    print("not a tringle")
else:
    print("a tringle")