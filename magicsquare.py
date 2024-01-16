def Upper_Triangular_Matrix(n, matrix):
    flag = True
    for i in range(1, n):
        for j in range(0, i-1):
            if(matrix[i][j]!=0):
                flag = False
                break
    return flag 


def Matrix_Addition(n, matrix1, matrix2):
    mat = []
    for i in range(0, n):
        list = []
        for j in range(0, n):
            list.append(0)
        mat.append(list)
            
    for i in range(0, n):
        for j in range(0, n):
            mat[i][j] = matrix1[i][j] + matrix2[i][j]
    return mat


def Matrix_Multiplication(n, matrix1, matrix2):
    mat = []
    for i in range(0, n):
        list = []
        for j in range(0, n):
            list.append(0)
        mat.append(list)    

    for i in range(0, n):
        for j in range(0, n):
            for k in range(0, n):
                mat[i][j] += matrix1[i][k]*matrix2[k][j]
    return mat

def Magic_Square(n, matrix):
    sum = 0
    for i in range(0, n):
        for j in range(0, n):
            if(i==j):
                sum += matrix[i][j]
                
    for i in range(0, n):
        sum1=0
        for j in range(0, n):
            sum1 += matrix[i][j]
        if(sum1!=sum):
            return False
        
    for j in range(0, n):
        sum1=0
        for i in range(0, n):
            sum1 += matrix[i][j]
        if(sum1!=sum):
            return False
    return True



n = int(input("Enter the number of rows of the matrix : "))

print("Take input of Matrix1:")
matrix1 = []
for i in range(0, n):
    list = []
    for j in range(0, n):
        k = int(input())
        list.append(k)
    matrix1.append(list)

print("Take input of Matrix2:")
matrix2 = []
for i in range(0, n):
    list = []
    for j in range(0, n):
        k = int(input())
        list.append(k)
    matrix2.append(list)



print("*----------Menu----------*")
print("0. Quit.")
print("1. Display the 2 Matrix.")
print("2. Add the two Matrix.")
print("3. Multiply the two Matrix. ")
print("4. Check wheather the Matrix is Upper Taiangular matrix or not.")
print("5. Check if the matrix is a magic square or not.")
print()

while(True):
    choice = int(input("Enter a choice : "))
    if(choice==0):
        print("Quit")
        break
    
    elif(choice==1):
        print("Matrix1: ")
        for row in matrix1:
            print(row)
        print()
        
        print("Matrix2: ")
        for row in matrix2:
            print(row)
            
    elif(choice==2):
        print("The Addition of the matrix1 and matrix2 is:")
        mat = Matrix_Addition(n, matrix1, matrix2)
        for row in mat:
            print(row)
            
    elif(choice==3):
        print("The multiplication of the matrix1 and matrix2 is:")
        mat = Matrix_Multiplication(n, matrix1, matrix2)
        for row in mat:
            print(row)
            
    elif(choice==4):
        if(Upper_Triangular_Matrix(n, matrix1)==1):
            print("The matrix is an Upper Triangular Matrix")
        else:
            print("The matrix is not an Upper Triangular Matrix")
            
    elif(choice==5):
        ans = Magic_Square(n, matrix1)
        if(ans):
            print("The Matrix is a Magic Square.")
        else:
            print("The matrix is not a Magix Square.")
    print()
      
