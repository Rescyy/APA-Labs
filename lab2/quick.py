import random as r

def quicksort(list):
    return quicksort_(list,0,len(list)-1)

def quicksort_(list,low,high):
    if low < high:
        i = low
        for j in range(low,high):
            if list[j] <= list[high]:
                list[i], list[j] = list[j],list[i]
                i += 1
        list[i], list[high] = list[high], list[i]
        quicksort_(list,low,i-1)
        quicksort_(list,i+1,high)
