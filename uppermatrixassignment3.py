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

    y=0
    s=0
    while(s<i):
        p=s
        while(p<i):
            if((L1[s][p])==0):
                y=1
                break
            p+=1
        s+=1
    
    s=1
    x=0
    while(s<i):
        p=0
        while(p<s):
            if((L1[s][p])!=0):
                x=1
                break
            p+=1
        s+=1
        
        
    if y==0 and x==0:
        print("It is an upper triangular matrix")
    else:
        print("It is not an upper triangular matrix")
#upper()

def trans():
    T=[]
    #T=[0]*[[0]*j for v in range(i)]
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
trans() 
     
"""  
        for s in range(1,i):                                            #Upper Triangular Matrix
            while(x<j):
                for p in range(0,x):
                    if L[s][p]!=0:
                        y=1
                x=x+1 """
    