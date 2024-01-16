def selection():
    n=int(input("Enter number of students:"))
    P=[]
    for i in range(n):
        x=float(input("Enter the percentage:"))
        P.append(x)
    print("Before Selection Sort :")
    print(P)
    print("After Selection Sort ")

    for i in range(0,n-1):
        mini=i
        for j in range(i+1,n):
            if(P[j]<P[mini]):
                mini=j

        t=P[i]
        P[i]=P[mini]
        P[mini]=t 
        print(P)                                                 # swap(mini,P[i])
  
def bubble():
    n2=int(input("Enter number of students:"))
    P2=[]
    for i in range(n2):
        x=float(input("Enter the percentage:"))
        P2.append(x)

    print("Before Bubble Sort :")
    print(P2)
    print("After Bubble Sort :")
    for i in range(0,n2-1):
        for j in range(0,n2-i-1):
            if(P2[j+1]<P2[j]):
                a=P2[j]
                P2[j]=P2[j+1]
                P2[j+1]=a
        print(P2) 

def insertion():
    n3=int(input("Enter number of students:"))
    P3=[]
    for i in range(n3):
        x=float(input("Enter the percentage:"))
        P3.append(x)

    print("Before Insertion Sort :")
    print(P3)
    print("After Insertion Sort :")
    for i in range(1,n3):
        z=P3[i]
        j=i-1
        while(j>=0):
            if(P3[j]>z):
                P3[j+1]=P3[j]
                P3[j]=z
                
            else:
                P3[j+1]=z
                break
            j=j-1
        print(P3)

def shell():
    n4=int(input("Enter number of students:"))
    P4=[]
    for i in range(n4):
        x=float(input("Enter the percentage:"))
        P4.append(x)
    print("Before Shell Sort :")
    print(P4)
    print("After Shell Sort :")
    gap=n4//2
    while(gap>0):
        i=gap
        while(i<n4):
            temp=P4[i]
            j=i-gap
            while(j>=0 and temp<P4[j]):
                P4[j+gap]=P4[j]
                j=j-gap
            P4[j+gap]=temp
            print(P4)
            i=i+gap
        gap=gap//2


selection()
#bubble() 
#insertion() 
shell()