n=int(input("Enter total number of students:"))
a=int(input("Enter the number of students playing cricket:"))
b=int(input("Enter the number of students playing badminton:"))
c=int(input("Enter the number of students playing football:"))
La=[]
Lb=[]
Lc=[]
P=[]
print("Enter all roll numbers of students:")
for i in range(0,n):
    w=int(input())
    P.append(w)

print("Enter roll no of cricketers:")
for i in range(0,a):
    m=int(input())
    La.append(m)
print("Enter roll no of badminton players:")
for i in range(0,b):
    m2=int(input())
    Lb.append(m2)
print("Enter roll no of football players:")
for i in range(0,c):
    m3=int(input())
    Lc.append(m3)
count1=0
cb=[]                                         #play both cricket and badminton
bf=[]                                         #play both badminton and football
cf=[]                                         #play both cricket and football
print("Roll No List of students who play both cricket and badminton: ")
for i in La:
    for j in Lb:
        if i==j:
            print(i)
            count1=count1+1                     #play both cricket and badminton
            cb.append(i)
count2=0
for i in Lb:
    for j in Lc:
        if i==j:
            count2=count2+1                     #play both badminton and football
            bf.append(i)
count3=0
for i in La:
    for j in Lc:
        if i==j:
            count3=count3+1                     #play both cricket and football
            cf.append(i)

# no of students who play all the sports
x=0
for i in La:
    for j in Lb:
        for k in Lc:
            if i==j and i==k and j==k:
                x=x+1                              #count of students playing all the sports                             



print("Roll No List of students who play either cricket or badminton but not both: ")
for i in P:
    if (i in La or i in Lb) and (i not in cb):
        print(i)
print("Number of students who play neither cricket nor badminton: ")   
a1=n-(a+b)+count1
print(a1)
print("Number of students who play cricket and football but not badminton: ")
a2=count3-x
print(a2)
y=n-(a+b+c-count1-count2-count3+x)                 #no of students who do not play any sport
print("Number of students who do not play any game: ")
print(y)

print("Roll Nos of students who play atleast one game: ")
for i in P:
    if i in La or i in Lb or i in Lc:
        print(i)

print("Roll Nos of students who play all three games: ")
for i in P:
    if i in La and i in Lb and i in Lc:
        print(i)





















""" print("Roll No List of students who play either cricket or badminton but not both: ")
for i in cb:
    for j in La:
        if i!=j:
            print(j)
for i in cb:
    for j in Lb:
        if i!=j:
            print(j)  """
        
       
""" count1=0 """
""" print("Number of students who play neither cricket nor badminton: ")
for i in Lc:
    for j in La:
        for k in Lc:
            if i!=j and i!=k:
                count1=count1+1
count1=count1+y   """
""" print(count1)                                    #adding no of students who play no game"""