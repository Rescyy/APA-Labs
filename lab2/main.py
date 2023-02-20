from timeit import default_timer as timer
from counting import countingsort
from heap import heapsort
from merge import mergesort
from quick import quicksort
from math import log10
import random as r
import matplotlib.pyplot as plt

def measure_time(func,n):
    print(len(n))
    start = timer()
    func(list(n))
    end = timer()
    print(func,end-start)
    return end-start

density = 10
def generate_random_list(n,max):
    return [r.randint(0,max) for i in range(n)]
lists = [generate_random_list(int(10**(i/density)), 10000) for i in range(density, 7 * density + 1)]
print("lists")
# lists10K = [generate_random_list(int(10**(i/density)), 10000) for i in range(density, 8 * density)]
# print("lists10k")
# lists100K = [generate_random_list(int(10**(i/density)), 100000) for i in range(density, 8 * density)]
# print("lists100K")
# lists1M = [generate_random_list(int(10**(i/density)), 1000000) for i in range(density, 8 * density - 1)]
# print("lists1M")
# lists10M = [generate_random_list(int(10**(i/density)), 10000000) for i in range(density, 8 * density - 1)]
# print("lists10M")
ox = [len(i) for i in lists]
log_ox = [log10(i) for i in ox]
# cox = [
#     [len(i) for i in lists10K],
#     [len(i) for i in lists100K],
#     [len(i) for i in lists1M],
#     [len(i) for i in lists10M]
# ]
# log_cox = [[log10(i) for i in j] for j in cox]
results = [
    [measure_time(heapsort, i) for i in lists],
    [measure_time(mergesort, i) for i in lists],
    [measure_time(quicksort, i) for i in lists]
]
# cresults = [
#     [measure_time(countingsort, i) for i in lists10K],
#     [measure_time(countingsort, i) for i in lists100K],
#     [measure_time(countingsort, i) for i in lists1M],
#     [measure_time(countingsort, i) for i in lists10M]
# ]
log_results = [[log10(i) for i in j] for j in results]
# log_cresults = [[log10(i) for i in j] for j in cresults]

plt.figure(1)
for i in results:
    plt.plot(ox,i)
# for i in range(4):
#     plt.plot(cox[i],cresults[i])
plt.plot
plt.grid(1)
plt.xlabel("n length of lists")
plt.ylabel("Time: seconds")
plt.legend([
    "Heap sort",
    "Merge sort",
    "Quick sort"
])
plt.figure(2)
for i in results:
    plt.plot(log_ox,i)
# for i in range(4):
#     plt.plot(log_cox[i],cresults[i])
plt.grid(1)
plt.xlabel("log(n) length of lists")
plt.ylabel("Time: seconds")
plt.figure(3)
for i in log_results:
    plt.plot(log_ox,i)
# for i in range(4):
#     plt.plot(log_cox[i],log_cresults[i])
plt.grid(1)
plt.xlabel("log(n) length of lists")
plt.ylabel("log(Time in seconds)")
plt.show()