from mpmath import mp
from timeit import default_timer as timer
import matplotlib.pyplot as plt

mp.dps = 10000

def matching_digits(a):
    temp_pi = str(a)
    PI_STR = str(mp.pi)
    i = 0
    while(i < mp.dps+1):
        if temp_pi[i] != PI_STR[i]:
            return i-1
        i += 1

def newton(iterations):
    sum = mp.mpf(3)
    term = sum
    i = 1
    while(i < iterations):
        t = 2*i
        term *= mp.mpf((t-1)**2)/8/i/(t+1)
        sum += term
        i += 1
    return sum

def measure_time(argument):
    start = timer()
    pi = newton(argument)
    end = timer()
    print(f"{mp.dps}, {argument}, {end-start}")
    return end-start, matching_digits(pi)

start = timer()
density = 100
oy_newton = []
ox_newton = []
ox_newton_points = []
oy_newton_points = []
for i in range(0,10001,density):
    time,digits = measure_time(i)
    mp.dps = digits + 70
    oy_newton.append(time)
    ox_newton.append(digits)
    if (i%(1000) == 0):
        ox_newton_points.append(digits)
        oy_newton_points.append(time)
plt.figure(1)
plt.plot(ox_newton, oy_newton, "b")
plt.plot(ox_newton_points, oy_newton_points, "bx")
mp.dps = 6050
oy_newton = []
ox_newton = []
ox_newton_points = []
oy_newton_points = []
for i in range(0,10001,density):
    time,digits = measure_time(i)
    oy_newton.append(time)
    ox_newton.append(digits)
    if (i%(1000) == 0):
        ox_newton_points.append(digits)
        oy_newton_points.append(time)
plt.plot(ox_newton, oy_newton, "g")
plt.plot(ox_newton_points, oy_newton_points, "gx")
plt.grid(1)
plt.xlabel("Digits of pi computed")
plt.ylabel("Time taken")
plt.title("Newton Algorithm")
plt.legend(["with precision adjusting", "1000 iterations mark", "without precision adjusting", "1000 iterations mark"])
end = timer()
print(end-start)
plt.show()