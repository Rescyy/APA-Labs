import random as r

def max_heapify(list, n, i):
    l = 2*i + 1
    r = 2*i + 2
    b = i
    if(l < n and list[l] > list[i]):
        b = l
    if(r < n and list[r] > list[b]):
        b = r
    if b != i:
        list[i],list[b] = list[b],list[i]
        max_heapify(list, n, b)

def buildMaxHeap(list):
    n = len(list)
    for i in range(n//2, -1, -1):
        max_heapify(list,n,i)

def heapsort(list):
    buildMaxHeap(list)
    n = len(list)
    newlist = []
    for i in range(n):
        newlist.append(list[0])
        list[0] = list[-1]
        list.pop()
        max_heapify(list,n - i - 1,0)
    return newlist
