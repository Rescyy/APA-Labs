#matrix algorithm

def matrix_multiplication5(A, B):
    a = A[0][0] * B[0][0] + A[0][1] * B[1][0]
    b = A[0][0] * B[0][1] + A[1][0] * B[1][1]
    c = A[0][0] * B[1][0] + A[0][1] * B[1][1]
    d = A[1][0] * B[0][1] + A[1][1] * B[1][1]
    A[0][0] = a
    A[0][1] = b
    A[1][0] = c
    A[1][1] = d

def power5(A, n):
    B = [[1,1],[1,0]]
    for i in range(n-2):
        matrix_multiplication5(A,B)

def fib5(n):
    if (not n):
        return n
    A = [[1,1],[1,0]]
    power5(A,n)
    return A[0][0]