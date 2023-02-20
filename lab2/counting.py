import random as r
from merge import mergesort 

def countingsort(list):
    a = list[0]
    for i in list:
        if a < i:
            a = i
    newlist = [0] * (a + 1)
    for i in list:
        newlist[i] += 1
    list.clear()
    for i in range(a):
        if newlist[i] > 0:
            for j in range(newlist[i]):
                list.append(i)
