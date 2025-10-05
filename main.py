import random
import time

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
    #returns a zero matrix of same size
    n = len(a1)
    return [[0 for _ in range(n)] for _ in range(n)]

#delete inner contents if implementing
def strassen(a1, a2):
    n = len(a1)
    return [[0 for _ in range(n)] for _ in range(n)]

#prints random 2D array
def rand2DArray():
    #we can change this later on for extra cred for n that isn't powers of 2
    n = 2**random.randint(1,5) #10 lwk took 3 minutes to run just once
    a = [[random.randint(-9,9) for x in range(n)] for x in range(n)]
    return a

def testing(a1, a2):
    start = time.perf_counter()
    res = classical(a1,a2)
    print("Classical Matrix Multipication Result:")
    for row in res:
        print(row)
    end = time.perf_counter()
    print("\nClassical Runtime: ", end-start, "seconds\n")

    start = time.perf_counter()
    res = naive(a1,a2)
    print("\nNaive Divide-and-Conquer Matrix Multiplication Result:")
    print(res)
    end = time.perf_counter()
    print("\nNaive Runtime: ", end-start, "Seconds\n")

    start = time.perf_counter()
    res = strassen(a1,a2)
    print("\nStrassen's Matrix Multiplication Result:")
    print(res)
    end = time.perf_counter()
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

    res = strassen(a1, a2)
    print("\nStrassen's Matrix Multiplication Result:")
    print(res)

if __name__ == "__main__":
    main()