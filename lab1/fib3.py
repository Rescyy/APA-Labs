#dynamic programming iterative algorithm

def fib3(n):
    list = [0,1]
    for i in range(2,n+1):
        list.append(list[i-1] + list[i-2])
    return list[n]