from __future__ import print_function
print("First Matrix Inputs")
row=int(input("Enter number of rows:"))
col=int(input("Enter number of columns:"))
A=[]
count=0
for i in range(row):
    row2=[]
    for j in range(col): 
        value=int(input("Enter a no:"))
        row2.append(value)
        if(value!=0):
            count=count+1
    A.append(row2)

print("First Matrix:")
for i in range(row):  
    print(A[i])  
print

#Sparse Matrix:
print("Sparse Matrix:")
A2=[]
row2=[]
row2.append(row)
row2.append(col)
row2.append(count)
A2.append(row2)

for p in range(row):
    
    for  s in range(col):
        row2=[]
        if(A[p][s]!=0):
            row2.append(p)
            row2.append(s)
            row2.append(A[p][s])       
            A2.append(row2)
    
for i in range(0,count+1):
    print(A2[i])
print

#TRANSPOSE OF SPARSE MATRIX
print("Transpose of Sparse Matrix:")
TA=[]
row2=[]
row2.append(col)
row2.append(row)
row2.append(count)
TA.append(row2)
for i in range(col):
    for k in range(1,count+1):
        row2=[]
        if(A2[k][1]==i):
            row2.append(A2[k][1])
            row2.append(A2[k][0])
            row2.append(A2[k][2])
            TA.append(row2)

for i in range(count+1):
    print(TA[i])
print

 #FAST TRANSPOSE
print("Fast Transpose of Sparse Matrix:")

Q=[]
row2=[]
row2.append(col)
row2.append(row)
row2.append(count)
Q.append(row2)

FT=[0]*count                            #count+1
for i in range(1,count+1):
    y=A2[i][1]
    FT[y]+=1

FT2=[]
FT2.append(1)
for i in range(0,count-1):  
    FT2.append(FT2[i]+FT[i])     

for i in range(1,count+1):
    row2=[]
    row2.append(A2[FT2[A2[i][1]]][1]) 
    row2.append(A2[FT2[A2[i][1]]][0]) 
    row2.append(A2[FT2[A2[i][1]]][2]) 
    Q.append(row2)
    FT2[A2[i][1]]+=1

for i in range(count+1):
    print(Q[i])
print 

""" FT2=[0]*(count)                           #count+1
FT2[0]=1
for i in range(1,count+1):                  #count+1
    FT2[i]=FT2[i-1]+FT[i-1] """

""" for i in range(1,count+1):
    Q.append([0,0,0])
    

for i in range(1,count+1):
    x=A2[i][1]
    t=FT2[x]
    Q[t][0]=A2[i][1]
    Q[t][1]=A2[i][0]
    Q[t][2]=A2[i][2]
    FT2[x]+=1 """



#SECOND MATRIX   
rowB=int(input("Enter number of rows of Second Matrix:"))
colB=int(input("Enter number of columns of Second Matrix:"))
B=[]
countB=0
for i in range(rowB):
    row2=[]
    for j in range(colB): 
        value=int(input("Enter a no:"))
        row2.append(value)
        if(value!=0):
            countB=countB+1
    B.append(row2)

print("Second Matrix:")
for i in range(rowB):  
    print(B[i])  
print

#Sparse Matrix:
print("Sparse Matrix:")
B2=[]
row2=[]
row2.append(rowB)
row2.append(colB)
row2.append(countB)
B2.append(row2)

for p in range(rowB):
    
    for  s in range(colB):
        row2=[]
        if(B[p][s]!=0):
            row2.append(p)
            row2.append(s)
            row2.append(B[p][s])       
            B2.append(row2)
    
for i in range(0,countB+1):
    print(B2[i])
print

#ADDITION OF SPARSE MATRICES
ADD=[]
v=0
if(row==rowB and col==colB):
    i=1
    j=1
    ADD.append([row,col,0])
    while(i<=count and j<=countB):
        if(A2[i][0]==B2[j][0]):                   #if row no is same
            if(A2[i][1]==B2[i][1]):               #if column no is same
                row2=[]
                row2.append(A2[i][0])
                row2.append(A2[i][1])
                row2.append(A2[i][2]+B2[i][2])
                ADD.append(row2)
                i+=1
                j+=1
                v+=1
            else:
                row2=[]
                if(A2[i][1]<B2[i][1]):
                    row2.append(A2[i][0])
                    row2.append(A2[i][1])
                    row2.append(A2[i][2])
                    ADD.append(row2)
                    i+=1
                    v+=1
                else:
                    row2.append(B2[i][0])
                    row2.append(B2[i][1])
                    row2.append(B2[i][2])
                    ADD.append(row2)
                    j+=1
                    v+=1
        else:
            if(A2[i][0]<B2[j][0]):
                row2=[]
                row2.append(A2[i][0])
                row2.append(A2[i][1])
                row2.append(A2[i][2])
                ADD.append(row2)
                i+=1
                v+=1
            else:
                row2=[]
                row2.append(B2[i][0])
                row2.append(B2[i][1])
                row2.append(B2[i][2])
                ADD.append(row2)
                j+=1
                v+=1
else:
            print("Addition is not possible ")
ADD[0][2]=v
print("The Added Matrix is:")
for i in range(v+1):
    print(ADD[i])
print