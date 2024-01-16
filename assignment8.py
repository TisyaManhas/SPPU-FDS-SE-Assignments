# n=int(input("Enter number of students:"))
P=[27,90,56,12,67,23,89,62]
# for i in range(7):
#     x=float(input("Enter the percentage:"))
#     P.append(x)
print("Before Quick Sort :")
print(P)
print("After Quick Sort :")
    
def partition(P,start,end):
    print("Partition")
    pivot=P[start]
    i=start
    j=end
    while(i<j):
        while(i<end and P[i]<=pivot):
            i+=1 
        print("i=",i)
        while(j>start and P[j]>pivot):
            j-=1   
        print("j=",j)                                   
        if(i<j):
            temp=P[i]
            P[i]=P[j]
            P[j]=temp                                                   #swap(P[i],P[j])
            print("Swapping ith and jth position",P)
    #if(i>=j):
    temp=P[start]
    P[start]=P[j]
    P[j]=temp 
    print("Swapping pivot and jth postion", P)
    return j
    
def quickSort(P,start,end):
    if(start<end):
        pi=partition(P,start,end)
        quickSort(P,start,pi-1)
        quickSort(P,pi+1,end)
        
quickSort(P,0,7)

    

        





            
    
