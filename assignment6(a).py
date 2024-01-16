n=int(input("Enter the number of students:"))
R=[]
print("Enter roll nos of students")
for i in range(n):
    roll=int(input("Enter Roll no:"))
    R.append(roll)
st=int(input("Enter the roll no of the student to be found: "))

#LINEAR SEARCH
count=0
print("By Linear Search")
for i in range(n):
    if(R[i]==st):
        count=1
        index=i
if(count==1):
     print("Student Found at index ", index+1)
else:
     print("Student not Found")

#SENTINEL SEARCH
R2=[]
R2=R
R2.append(st)
count2=0
i=0
print("By Sentinel Search")
while(R2[i]!=st):
     i+=1
if(i!=len(R2)-1):
     print("Student Found")
else:
     print("Student not Found")








 