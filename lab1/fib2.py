#space optimized iterative algorithm

def fib2(n):
    a = 0
    b = 1
    for i in range(n):
        temp = b
        b = a + b
        a = temp
    return a