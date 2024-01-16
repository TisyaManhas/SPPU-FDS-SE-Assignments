m=int(input("Enter highest degree of 1st polynomial:"))
p1=[]
p=int(input("Enter no terms in 1st polynomial:"))
for i in range(m+1):
    p1.append(0)
    
for i in range(p):
    index=int(input("Enter index"))
    coeff=int(input("Enter the non zero coeff"))
    p1[index]=coeff

def output(poly,k):
    for i in range(len(poly)):
        if(poly[i]!=0 and k!=1):
            print(str(poly[i])+"x^"+str(i)+"+", end="")
            k-=1
        elif(poly[i]!=0 and k==1):
            print(str(poly[i])+"x^"+str(i))
output(p1,p)

def evaluate(poly,val):
    temp=0
    for i in range(len(poly)):
        temp+=poly[i]*(val**i)
    print("f(x): ",end="")
    print(temp)
x=int(input("Enter the value: "))
evaluate(p1,x)

m2=int(input("Enter highest degree of 2nd polynomial:"))
p2=[]
pp=int(input("Enter no terms in 2nd polynomial:"))
for i in range(m2+1):
    p2.append(0)
    
for i in range(pp):
    index=int(input("Enter index"))
    coeff=int(input("Enter the non zero coeff"))
    p2[index]=coeff

def sum(poly1,poly2):
    a=len(poly1)
    b=len(poly2)
    temp=[]
    cnt=0
    if(a<=b):
        for i in range(a):
            temp.append(poly1[i]+poly2[i])
        for i in range(a,b):
            temp.append(poly2[i])
    else:
        for i in range(b):
            temp.append(poly1[i]+poly2[i])
        for i in range(b,a):
            temp.append(poly1[i])
    
    for i in range (len(temp)):
       if(temp[i]!=0):
           cnt+=1 
    output(temp,cnt)
    
sum(p1,p2)

def multiplication(poly1,poly2):
    a=len(poly1)
    b=len(poly2)
    temp=[0]*(a+b+1)
    cnt=0
    
    for i in range(a):
        for j in range(b):
            temp[i+j]+=poly1[i]*poly2[j]
            
    for i in range(len(temp)):
        if(temp[i]!=0):
            cnt+=1
    output(temp,cnt)

multiplication(p1,p2)