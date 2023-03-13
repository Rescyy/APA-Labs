from timeit import default_timer as timer
from algorithms import algorithm_list
import matplotlib.pyplot as plt
from math import log10

def measure_time(func,n):
    start = timer()
    func(n)
    end = timer()
    # print(end-start,n)
    return end-start

def generate_list(a):
    return [int(10**(i/density)) for i in range(density, a + 1)]

density = 4
evaluated = range(5)
ox = [[]] * 5
ox[0] = generate_list(density*7)
ox[1] = generate_list(density*7-2)
ox[2] = generate_list(density*5-2)
ox[3] = generate_list(density*4)
ox[4] = generate_list(density*5)
logox = [[]] * 5
for i in evaluated:
    logox[i] = [log10(x) for x in ox[i]]
oy = [[]] * 5
logoy = [[]] * 5
for i in evaluated:
    oy[i] = ([measure_time(algorithm_list[i], x) for x in ox[i]])
    print(i)
    logoy[i] = ([log10(x) for x in oy[i]])
plt.figure(1)
for i in evaluated:
    plt.plot(ox[i],oy[i])
plt.legend([f"Algorithm {i}" for i in range(1,6)])
plt.xlabel("Number of elements evaluated")
plt.ylabel("Time execution in seconds")
plt.figure(2)
for i in evaluated:
    plt.plot(logox[i], oy[i])
plt.xlabel("Logarithmic number of elements evaluated")
plt.ylabel("Time execution in seconds")
plt.figure(3)
for i in evaluated:
    plt.plot(logox[i], logoy[i])
plt.xlabel("Logarithmic number of elements evaluated")
plt.ylabel("Logarithmic time execution in seconds")
plt.show()