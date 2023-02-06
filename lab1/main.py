from timeit import default_timer as timer
from fib1 import fib1
from fib2 import fib2
from fib3 import fib3
from fib4 import fib4
from fib5 import fib5
from fib6 import fib6
from fib7 import fib7
from fib8 import fib8
import matplotlib.pyplot as plt
import math as m

def measure_time(func,n):
    start = timer()
    func(n)
    end = timer()
    return end-start

def loglist(list):
    newlist = []
    for i in list:
        newlist.append(m.log10(i))
    return newlist

list_ox1 = [1,2,4,8,12,16,20,25,30,33]
list_ox2 = [1,5,10,33,100,333,1000,3333,10000,25000,50000,100000,150000,200000,300000,350000]
list_ox3 = [1,5,10,33,100,333,1000,3333,10000,25000,50000,100000,150000,200000]
list_ox4 = [1,5,10,33,100,333,666,1000,1333,1474]
list_ox5 = [1,5,10,33,100,333,1000,3333,10000,25000,50000,100000,115000]
list_ox6 = [1,5,10,33,100,333,1000,3333,10000,33333,66666,100000,250000,500000,750000,1000000,2000000,3000000,4000000]
list_ox7 = [1,5,10,33,100,333,1000,3333,10000,33333,66666,100000,250000,500000,750000,1000000,2000000,3000000,4000000,5000000,6000000,7000000,8000000,9000000,10000000]
list_ox8 = [1,5,10,33,100,333,1000,3333,10000,33333,66666,100000,250000,500000,750000,1000000,2000000,3000000,4000000,5000000,6000000,7000000,8000000,9000000,10000000]
list_oy1 = []
list_oy2 = []
list_oy3 = []
list_oy4 = []
list_oy5 = []
list_oy6 = []
list_oy7 = []
list_oy8 = []

for i in list_ox1:
    list_oy1.append(measure_time(fib1,i))
for i in list_ox2:
    list_oy2.append(measure_time(fib2,i))
for i in list_ox3:
    list_oy3.append(measure_time(fib3,i))
for i in list_ox4:
    list_oy4.append(measure_time(fib4,i))
for i in list_ox5:
    list_oy5.append(measure_time(fib5,i))
for i in list_ox6:
    list_oy6.append(measure_time(fib6,i))
for i in list_ox7:
    list_oy7.append(measure_time(fib7,i))
for i in list_ox8:
    list_oy8.append(measure_time(fib8,i))

# plt.figure(1)
# plt.plot(loglist(list_ox1),list_oy1)
# plt.plot(loglist(list_ox2),list_oy2)
# plt.plot(loglist(list_ox3),list_oy3)
# plt.plot(loglist(list_ox4),list_oy4)
# plt.plot(loglist(list_ox5),list_oy5)
# plt.plot(loglist(list_ox6),list_oy6)
# plt.plot(loglist(list_ox7),list_oy7)
# plt.plot(loglist(list_ox8),list_oy8)
# plt.grid(1)
# plt.xlabel("10^n-th Fibonacci number")
# plt.ylabel("Time: seconds")
# plt.legend([
# "1.Recursive",
# "2.Space Optimized",
# "3.Dynamic Memory",
# "4.Binet Formula",
# "5.Naive Matrix",
# "6.Optimised Matrix",
# "7.Fibonacci Doubling (List)", 
# "8.Fibonacci Doubling (Directory)"])
# plt.figure(2)
# plt.plot(list_ox1,list_oy1)
# plt.plot(list_ox2,list_oy2)
# plt.plot(list_ox3,list_oy3)
# plt.plot(list_ox4,list_oy4)
# plt.plot(list_ox5,list_oy5)
# plt.plot(list_ox6,list_oy6)
# plt.plot(list_ox7,list_oy7)
# plt.plot(list_ox8,list_oy8)
# plt.grid(1)
# plt.xlabel("nth Fibonacci number")
# plt.ylabel("Time: seconds")
# plt.legend([
# "1.Recursive",
# "2.Space Optimized",
# "3.Dynamic Memory",
# "4.Binet Formula",
# "5.Naive Matrix",
# "6.Optimised Matrix",
# "7.Fibonacci Doubling (List)", 
# "8.Fibonacci Doubling (Directory)"])

plt.figure(3)
plt.plot(loglist(list_ox1),loglist(list_oy1))
plt.plot(loglist(list_ox2),loglist(list_oy2))
plt.plot(loglist(list_ox3),loglist(list_oy3))
plt.plot(loglist(list_ox4),loglist(list_oy4))
plt.plot(loglist(list_ox5),loglist(list_oy5))
plt.plot(loglist(list_ox6),loglist(list_oy6))
plt.plot(loglist(list_ox7),loglist(list_oy7))
plt.plot(loglist(list_ox8),loglist(list_oy8))
plt.grid(1)
plt.xlabel("10^n-th Fibonacci number")
plt.ylabel("Time: log10(seconds)")
plt.show()
