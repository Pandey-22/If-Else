classheld=int(input("how many classes are held"))
classattend=int(input("how many classes are attended by student"))
per=classattend/classheld*100
print("total percentage of this student is",per,"%")
if per<75:
    print("this student cannot be sit in final exam")
else:
    print("this student can be sit in final exam")   