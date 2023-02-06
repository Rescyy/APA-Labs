#binet formula

import numpy as np
gold = 1.618033988749895
ngold = 0.6180339887498949
sqrtfive = 2.23606797749979

def fib4(n):
    if(n%2):
        return (np.power(gold,n) + np.power(ngold,n))/sqrtfive
    else:
        return (np.power(gold,n) - np.power(ngold,n))/sqrtfive