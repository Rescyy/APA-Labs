#optimised matrix algorithm

def matrix_multiplication6(A, B):
    a = A[0][0] * B[0][0] + A[0][1] * B[1][0]
    b = A[0][0] * B[0][1] + A[1][0] * B[1][1]
    c = A[0][0] * B[1][0] + A[0][1] * B[1][1]
    d = A[1][0] * B[0][1] + A[1][1] * B[1][1]
    A[0][0] = a
    A[0][1] = b
    A[1][0] = c
    A[1][1] = d

def power6(A, n):
    if(n <= 1):
        return
    B = [[1,1],[1,0]]
    power6(A, n//2)
    matrix_multiplication6(A,A)
    if(n%2):
        matrix_multiplication6(A, B)

def fib6(n):
    if (not n):
        return n
    A = [[1,1],[1,0]]
    power6(A,n-1)
    return A[0][0]
