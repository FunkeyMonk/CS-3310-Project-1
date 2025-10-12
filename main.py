import random
import time
#HELPER METHODS

#O(n^2) time complexity
def add(A, B):
    n = len(A)
    C = [[0 for _ in range(n)] for _ in range(n)] #fill w/ 0s
    for i in range(n):
        for j in range(n):
            C[i][j] = A[i][j] + B[i][j]
    return C

#O(n^2) time complexity
def subtract(A, B):
    n = len(A)
    C = [[0 for _ in range(n)] for _ in range(n)] #fill w/ 0s
    for i in range(n):
        for j in range(n):
            C[i][j] = A[i][j] - B[i][j]
    return C

#Strassen needs matrices to be of size 2^k x 2^k
def pad_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    
    # Find the next power of two for the larger dimension
    size = 1
    while size < max(rows, cols):
        size *= 2
    
    new_matrix = [[0 for _ in range(size)] for _ in range(size)]
    #copy og matrix into padded
    for i in range(rows):
        for j in range(cols):
            new_matrix[i][j] = matrix[i][j]
            
    return new_matrix

# Removes the padding from a matrix to return it to its original size
def unpad_matrix(matrix, original_rows, original_cols):
    return [row[:original_cols] for row in matrix[:original_rows]]

def combine_quadrants(C11, C12, C21, C22):
    # assuming submatrices are the same size
    mid = len(C11)
    n = 2 * mid
    
    C = [[0 for _ in range(n)] for _ in range(n)]
    
    # C11
    for i in range(mid):
        for j in range(mid):
            C[i][j] = C11[i][j]
            
    # C12
    for i in range(mid):
        for j in range(mid):
            C[i][j + mid] = C12[i][j]
            
    # C21
    for i in range(mid):
        for j in range(mid):
            C[i + mid][j] = C21[i][j]
            
    # C22
    for i in range(mid):
        for j in range(mid):
            C[i + mid][j + mid] = C22[i][j]
            
    return C


def classical(a1, a2):
    #check if matrix dimensions are valid; might keep in if manual entry is implemented lateron
    n = len(a1)
    if len(a2) != n or len(a1[0]) != len(a2):
        raise ValueError("Incompatible matrix sizes")
    
    #initialize result w/ 0s
    result = [[0 for val in range(n)] for val in range(n)]

    for i in range(n): #go through rows of a1
        for j in range(n): # go through columns of a2
            total = 0
            for k in range(n): #the dot prod of row i & col j
                total += a1[i][k] * a2[k][j]
            result[i][j] = total

    return result

#I put placeholders in this; delete the contents if implementing
def naive(a1, a2):
    n = len(a1)

    # Base case: if matrix is 1x1, perform simple multiplication
    if n == 1:
        return [[a1[0][0] * a2[0][0]]]
    

    # Split matrices into quadrants
    mid = n // 2
    #A11 is top left quadrant in matrix A, A12 is top right in matrix A, etc...
    A11 = [row[:mid]  for row in a1[:mid]]
    A12 = [row[mid:]  for row in a1[:mid]]
    A21 = [row[:mid]  for row in a1[mid:]]
    A22 = [row[mid:]  for row in a1[mid:]]

    B11 = [row[:mid]  for row in a2[:mid]]
    B12 = [row[mid:]  for row in a2[:mid]]
    B21 = [row[:mid]  for row in a2[mid:]]
    B22 = [row[mid:]  for row in a2[mid:]]


    # 8 recursive multiplications, do naive within the addition to make code clean and concise
    C11 = add(naive(A11, B11), naive(A12, B21))
    C12 = add(naive(A11, B12), naive(A12, B22))
    C21 = add(naive(A21, B11), naive(A22, B21))
    C22 = add(naive(A21, B12), naive(A22, B22))

    # Recombine qudrants into matrix
    C = combine_quadrants(C11, C12, C21, C22)
    return C



def strassen(a1, a2):
    n = len(a1)

    # Base case: if matrix is 1x1, perform simple multiplication
    if n == 1:
        return [[a1[0][0] * a2[0][0]]]

    # Divide matrices into four sub-matrices
    
    '''
    [row[:mid] for row in a1[:mid]]
          ^columns            ^rows
    '''
    
    mid = n // 2
    A11 = [row[:mid]  for row in a1[:mid]]
    A12 = [row[mid:]  for row in a1[:mid]]
    A21 = [row[:mid]  for row in a1[mid:]]
    A22 = [row[mid:]  for row in a1[mid:]]

    B11 = [row[:mid]  for row in a2[:mid]]
    B12 = [row[mid:]  for row in a2[:mid]]
    B21 = [row[:mid]  for row in a2[mid:]]
    B22 = [row[mid:]  for row in a2[mid:]]

    # Calculate the seven products recursively
    P1 = strassen(add(A11, A22), add(B11, B22))
    P2 = strassen(add(A21, A22), B11)
    P3 = strassen(A11, subtract(B12, B22))
    P4 = strassen(A22, subtract(B21, B11))
    P5 = strassen(add(A11, A12), B22)
    P6 = strassen(subtract(A21, A11), add(B11, B12))
    P7 = strassen(subtract(A12, A22), add(B21, B22))

    # Combine the products to form the result sub-matrices
    C11 = add(subtract(add(P1, P4), P5), P7)
    C12 = add(P3, P5)
    C21 = add(P2, P4)
    C22 = add(add(subtract(P1, P2), P3), P6)

    # Combine the result sub-matrices into the final matrix
    C = combine_quadrants(C11, C12, C21, C22)

    return C

#prints random 2D array
def rand2DArray():
    #we can change this later on for extra cred for n that isn't powers of 2
    
    #Colin Note: padding allows for non 2^k sizes
    n = random.randint(2,3)**random.randint(1,5) #10 lwk took 3 minutes to run just once
    a = [[random.randint(-9,9) for x in range(n)] for x in range(n)]
    return a

def testing(a1, a2):
    
    a1 = pad_matrix(a1)
    a2 = pad_matrix(a2)

    start = time.perf_counter()
    res = classical(a1,a2)
    end = time.perf_counter()
    print("Classical Matrix Multipication Result:")
    print(unpad_matrix(res, len(a1), len(a2)))
    print("\nClassical Runtime: ", end-start, "seconds\n")


    start = time.perf_counter()
    res = naive(a1,a2)
    end = time.perf_counter()
    print("\nNaive Divide-and-Conquer Matrix Multiplication Result:")
    print(unpad_matrix(res, len(a1), len(a2)))
    print("\nNaive Runtime: ", end-start, "Seconds\n")

    start = time.perf_counter()
    res = strassen(a1,a2)
    end = time.perf_counter()
    print("\nStrassen's Matrix Multiplication Result:")
    print(unpad_matrix(res, len(a1), len(a2)))
    print("\nStrassen Runtime: ", end-start, "seconds\n")

def main():
    print("\n\n-----------TESTING-----------")
    for i in range(1,4):
        print("\nTEST ", i)
        r1 = rand2DArray()
        r2 = rand2DArray()
        #checks to see if the rand2D array is able to be multiplied
        #can be changed if we want to do extra credit
        while(len(r1[0]) != len(r2)):
            r2 = rand2DArray()
        testing(r1, r2)
        print("\n")
    print("\n\n\n\n\n")

    #----------------------------Report Things--------------------
    print("\nReport:")
    a1 = [[2,0,-1,6],
          [3,7,8,0],
          [-5,1,6,-2],
          [8,0,1,7]]
    
    a2 = [[0,1,6,3],
          [-2,8,7,1],
          [2,0,-1,0],
          [9,1,6,-2]]


    res = classical(a1,a2)
    print("\nClassical Matrix Multipication Result:")
    print(res)
    
    res = naive(a1,a2)
    print("\nNaive Divide-and-Conquer Matrix Multiplication Result:")
    print(res)

    res = strassen(pad_matrix(a1),pad_matrix(a2))
    print("\nStrassen's Matrix Multiplication Result:")
    print(unpad_matrix(res, len(a1), len(a2)))

if __name__ == "__main__":
    main()