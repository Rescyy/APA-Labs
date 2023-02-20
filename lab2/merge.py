import random as r

def mergesort(list):
    n = len(list)
    if(n == 1):
        return list
    left = mergesort(list[:n//2])
    right = mergesort(list[n//2:])
    newlist = []
    leftlen = n//2
    rightlen = n//2 + n%2
    i = 0
    j = 0
    while(i < leftlen or j < rightlen):
        if left[i] > right[j]:
            newlist.append(right[j])
            j += 1
            if j == rightlen:
                for k in left[i:]:
                    newlist.append(k)
                break
        else:
            newlist.append(left[i])
            i += 1
            if i == leftlen:
                for k in right[j:]:
                    newlist.append(k)
                break
    return newlist