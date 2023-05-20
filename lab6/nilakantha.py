from mpmath import mp
from timeit import default_timer as timer
import matplotlib.pyplot as plt

mp.dps = 20

def matching_digits(a):
    temp_pi = str(a)
    PI_STR = str(mp.pi)
    i = 0
    while(i < mp.dps+1):
        if temp_pi[i] != PI_STR[i]:
            return i-1
        i += 1

def nilakantha(iterations):
    i = 0
    sum = 3
    k = 2
    while(i < iterations):
        sum += ((-1)**(i))*mp.mpf(4)/(k)/(k+1)/(k+2)
        i += 1
        k += 2
    return sum

def measure_time(argument):
    start = timer()
    pi = nilakantha(argument)
    end = timer()
    print(f"{argument}, {end-start}")
    return end-start, matching_digits(pi)
    
density = 1000
plt.figure(1)
oy_nilak = []
ox_nilakoy_nilak = []
ox_nilakoy_nilak_points = []
oy_nilak_points = []
for i in range(0,100001,density):
    time,digits = measure_time(i)
    oy_nilak.append(time)
    ox_nilakoy_nilak.append(digits)
    if (i%10000 == 0):
        ox_nilakoy_nilak_points.append(digits)
        oy_nilak_points.append(time)
plt.plot(ox_nilakoy_nilak, oy_nilak, "g")
plt.plot(ox_nilakoy_nilak_points, oy_nilak_points, "gx")
plt.grid(1)
plt.xlabel("Digits of pi computed")
plt.ylabel("Time taken")
plt.title("Nilakantha Algorithm")
plt.legend(["20 digits precision", "10000 iterations mark"])
plt.show()