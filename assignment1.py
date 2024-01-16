""" Write a Python program to store marks scored in subject “Fundamental of Data Structure” by N students in the class.
Write functions to compute following:
a) The average score of class b) Highest score and lowest score of class
c) Count of students who were absent for the test 
d) Display mark with highest frequency
e) Percentages of passed and failed students
f) Find the top three highest scores. """

n=int(input("Enter the number of students:"))
M=[]
sum=0
count=0
for i in range(n):
    x=int(input("Enter marks out of 100:"))
    if(x>=0):
        sum+=x
        M.append(x)
    else:
        count+=1

avg=sum/(n-count)
print("Average Score :")
print(avg) 

highest=max(M)
least=min(M)
print("Higest score: ")
print(highest)
print("Least Score :")
print(least)

print("Number of students who were absent: ")
print(count)

p=0
f=0
for i in M:
    if(i>=60):
        p=p+1
    else:
        f=f+1
pp=p/(n-count)*100
fp=f/(n-count)*100
print("Percentage of pass students:",pp)
print("Percentage of fail students:",fp)

print("Marks of 3 toppers:")
freq={}
for i in M:
    if(i in freq):
        freq[i]+=1
    else:
        freq[i]=1
key1=list(freq.keys())
val1=list(freq.values())
key1.sort()
val1.sort()
print(key1[len(key1)-1])
print(key1[len(key1)-2])
print(key1[len(key1)-3])
for key,value in freq.items():
    if value==val1[len(val1)-1]:
        print("marks with highest frequency:",key)