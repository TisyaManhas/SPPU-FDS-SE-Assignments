n=int(input("Enter the number of students:"))
R=[]
print("Enter roll nos of students")
for i in range(n):
    roll=int(input("Enter Roll no:"))
    R.append(roll)
st=int(input("Enter the roll no of the student to be found: "))

R.sort()
#BINARY SEARCH
print("By Binary Search")
low=0
high=n-1

count=0
while(low<=high):
    mid=(low+high)//2
    if(R[mid]==st):
        count=1
        break
    else:
        if(st<R[mid]):
            high=mid-1
        else:
            low=mid+1
if(count==1):
    print("Student Found")
else:
    print("Student Not Found")

#FIBONACCI SEARCH
print("By Fibonacci Search")
fibm2=0
fibm1=1
fibm=1
x=0
while(fibm<n):
    fibm2=fibm1
    fibm1=fibm
    fibm=fibm1+fibm2
offset=0

while(fibm>1):
    i=min((offset+fibm2),n-1)
    if(R[i-1]==st):  
        x=1
        index=i
        break
    else:
        if(R[i-1]<st):
            fibm=fibm1
            fibm1=fibm2
            fibm2=fibm-fibm1
            offset=i
        else:
            fibm=fibm2
            fibm1=fibm1-fibm2
            fibm2=fibm2-fibm1
if(x==1):
    print("Student Found")
else:
    print("Student Not Found")


         

        


    

    