#recursive algorithm

def fib1(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib1(n-1) + fib1(n-2)