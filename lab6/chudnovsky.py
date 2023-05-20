from mpmath import mp
from timeit import default_timer as timer
import matplotlib.pyplot as plt

mp.dps = 50

def matching_digits(a):
    temp_pi = str(a)
    PI_STR = str(mp.pi)
    i = 0
    while(i < mp.dps+1):
        if temp_pi[i] != PI_STR[i]:
            return i-1
        i += 1

def chudnovsky(iterations):
    i = 0
    C = 426880*mp.sqrt(10005)
    L = mp.mpf(13591409)
    X = mp.mpf(1)
    K = mp.mpf(-6)
    M = mp.mpf(1)
    sum = L
    while(i < iterations):
        L += 545140134
        X *= -262537412640768000
        K += 12
        M *= (K**3-16*K)/((i+1)**3)
        i += 1
        sum += M*L/X
    return C*(sum**-1)

def measure_time(argument):
    start = timer()
    pi = chudnovsky(argument)
    end = timer()
    print(f"{argument}, {end-start}")
    return end-start, matching_digits(pi)
    
density = 10
oy_chud = []
ox_chud = []
ox_chud_points = []
oy_chud_points = []
for i in range(0,701,density):
    time,digits = measure_time(i)
    mp.dps = digits + 15*density + 1
    oy_chud.append(time)
    ox_chud.append(digits)
    if (i%(density*10) == 0):
        ox_chud_points.append(digits)
        oy_chud_points.append(time)
plt.figure(1)
plt.plot(ox_chud, oy_chud, "b")
plt.plot(ox_chud_points, oy_chud_points, "bx")
mp.dps = 10000
oy_chud = []
ox_chud = []
ox_chud_points = []
oy_chud_points = []
for i in range(0,701,density):
    time,digits = measure_time(i)
    oy_chud.append(time)
    ox_chud.append(digits)
    if (i%(density*10) == 0):
        ox_chud_points.append(digits)
        oy_chud_points.append(time)
plt.plot(ox_chud, oy_chud, "g")
plt.plot(ox_chud_points, oy_chud_points, "gx")
plt.grid(1)
plt.xlabel("Digits of pi computed")
plt.ylabel("Time taken")
plt.title("Chudnovsky Algorithm")
plt.legend(["with precision adjusting", "100 iterations mark", "without precision adjusting", "100 iterations mark"])
plt.show()
