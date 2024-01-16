i=int(input("Enter i: "))
j=int(input("Enter j: "))
L=[]

for s in range(0,i):
    row=[]
    for p in range(0,j): 
        m=int(input("Enter a no:"))
        row.append(m)
    L.append(row)

L1=[]
L1=L
def upper():
    for p in range(0,i):                                        
        print(L[p] )
    print
    x=0
    y=0
    for s in range(1,i):                                            #Upper Triangular Matrix
        while(x<j):
            for p in range(0,x):
                if L[s][p]!=0:
                    y=1
            x=x+1
    if y==0:
        print("It is an upper triangular matrix")
    else:
        print("It is not an upper triangular matrix")

def diagsum():
    sum=0
    for s in range(0,i):                                         #Sum of Diagonal Elements
        sum=sum+L[s][s]
    print("Sum of diagonal elements:")
    print(sum)

def trans():
    T=[]
    for s in range(0,i):
        r=[]
        for p in range(0,j):
            v=0
            r.append(v)
        T.append(r)
    for s in range(0,i):                                         #Transpose
        for p in range(0,j):
            T[s][p]=L[p][s]
    print("Transpose of matrix: ")
    for s in range(0,i):         
        print(T[s] )
    print

upper()
diagsum()
trans()
L2=[]                                                          #SECOND MATRIX
print("Enter values of Second Matrix")
for s in range(0,i):
    row2=[]
    for p in range(0,j): 
        m2=int(input("Enter a no:"))
        row2.append(m2)
    L2.append(row2)

def sum():
    A=[]                                                           #Sum of Two Matrix
    print("Added Matrix")
    for s in range(0,i):
        row3=[]
        for p in range(0,j):
            sum1=L1[s][p]+L2[s][p]
            row3.append(sum1)
        A.append(row3)
    for p in range(0,i):                                           #Added Matrix       
        print(A[p] )
    print

def diff():
    S=[]
    print("Subtracted Matrix")
    for s in range(0,i):
        row3=[]
        for p in range(0,j):
            diff=L2[s][p]-L1[s][p]
            row3.append(diff)
        S.append(row3)
    for p in range(0,i):                                           #Subtracted Matrix       
        print(S[p] )
    print


""" for s in range(0,i):
    r=[]
    for p in range(0,j):
        v=0
        r.append(v)
    M.append(r) """

def prod():
    M=[]
    for s in range(0,i):
        r=[0]*j
        # for p in range(0,j):
        #     v=0
        #     r.append(v)
        M.append(r)
    print("Product of the two Matrix")
    for s in range(0,i):
        for p in range(0,j):
            for k in range(0,j):
                M[s][p]+= (L1[s][k]*L2[k][p])                                                #Multiplied Matrix       
    print(M)
print

sum()
diff() 
prod()
#Saddle point
print("Saddle points are:")
def saddle():
    for s in range(0,i):
        for p in range(0,j):
            if(L1[s][p]==min(L1[s])):                       # and L1[s][p]==max(L1[p])):
                maxi=L1[s][p]
                for d in range(0,i):
                    if(L1[d][p]>=maxi):
                        maxi=L1[d][p]
                        g=d
                        w=p
    print(g,w)
saddle()




    





""" for s in range(0,i):
    for p in range(0,j):
        m=int(input("Enter a no:"))
        a[i][j]=m
 """