import random
import time

def classical(a1, a2):
    return 

def naive(a1, a2):
    return 

def strassen(a1, a2):
    return 

#prints random 2D array
def rand2DArray():
    n = 2**random.randint(1,10)
    a = [[random.randint(-9,9) for x in range(n)] for x in range(n)]
    return a

def testing(a1, a2):
    start = time.perf_counter()
    res = classical(a1,a2)
    print("Classical Matrix Multipication Result:")
    print(res)
    end = time.perf_counter()
    print("Classical Runtime: ", end-start)

    start = time.perf_counter()
    res = naive(a1,a2)
    print("Naive Divide-and-Conquer Matrix Multiplication Result:")
    print(res)
    end = time.perf_counter()
    print("Naive Runtime: ", end-start)

    start = time.perf_counter()
    res = strassen(a1,a2)
    print("Strassen's Matrix Multiplication Result:")
    print(res)
    end = time.perf_counter()
    print("Strassen Runtime: ", end-start)

def main():
    print("-----------TESTING-----------")
    for i in range(1,4):
        print("TEST ", i)
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
    print("Report:")
    a1 = [[2,0,-1,6],
          [3,7,8,0],
          [-5,1,6,-2],
          [8,0,1,7]]
    
    a2 = [[0,1,6,3],
          [-2,8,7,1],
          [2,0,-1,0],
          [9,1,6,-2]]


    res = classical(a1,a2)
    print("Classical Matrix Multipication Result:")
    print(res)
    
    res = naive(a1,a2)
    print("Naive Divide-and-Conquer Matrix Multiplication Result:")
    print(res)

    res = strassen(a1, a2)
    print("Strassen's Matrix Multiplication Result:")
    print(res)

if __name__ == "__main__":
    main()