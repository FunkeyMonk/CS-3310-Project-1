import random

def classical(a1, a2):
    return 

def naive(a1, a2):
    return 

def strassen(a1, a2):
    return 

def rand2DArray():
    n = 2**random.randint(1,10)
    a = [[random.randint(-9,9) for x in range(n)] for x in range(n)]
    return a

def main():
    a1 = [[2,0,-1,6],
          [3,7,8,0],
          [-5,1,6,-2],
          [8,0,1,7]]
    
    a2 = [[0,1,6,3],
          [-2,8,7,1],
          [2,0,-1,0],
          [9,1,6,-2]]
    

    print(rand2DArray())


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