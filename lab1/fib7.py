#matrix fibonacci identity algorithm using memory array
#fast doubling

def fib(n,f):
    if(n == 0):
        return 0
    if(n == 1 or n == 2):
        return 1
    if(f[n]):
        pass
    elif(n%2):
        f[n] = fib(n//2,f)**2 + fib(n//2+1,f)**2
    else:
        f[n] = (2 * fib(n//2-1,f) + fib(n//2,f)) * fib(n//2,f)
    return f[n]

def fib7(n):
    f = [0] * (n+1)
    return fib(n,f)

fib7(2**20)