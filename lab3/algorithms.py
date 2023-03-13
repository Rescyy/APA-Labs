from math import isqrt
from line_profiler import LineProfiler

def algorithm1(n):
    c = [False] + [True] * n
    i = 2
    while i <= n:
        if c[i]:
            j = 2 * i
            while j <= n:
                c[j] = False
                j += i
        i += 1
    return [i for i in range(1,len(c)) if c[i]]

def algorithm2(n):
    c = [False] + [True] * n
    i = 2
    while i <= n:
        j = 2 * i
        while j <= n:
            c[j] = False
            j += i
        i += 1
    return [i for i in range(1,len(c)) if c[i]]

def algorithm3(n):
    c = [False] + [True] * n
    i = 2
    while i <= n:
        if c[i]:
            j = i + 1
            while j <= n:
                if not j%i:
                    c[j] = False
                j += 1
        i += 1
    return [i for i in range(2,len(c)) if c[i]]

def algorithm4(n):
    c = [False] + [True] * n
    i = 2
    while i <= n:
        j = 2
        while j < i:
            if not i%j:
                c[i] = False
            j += 1
        i += 1
    return [i for i in range(1,len(c)) if c[i]]

def algorithm5(n):
    c = [False] + [True] * n
    i = 2
    while i <= n:
        j = 2
        while j <= isqrt(i):
            if not i%j:
                c[i] = False
            j += 1
        i += 1
    return [i for i in range(1,len(c)) if c[i]]

algorithm_list = [algorithm1, algorithm2, algorithm3, algorithm4, algorithm5]


