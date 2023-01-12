import os
import time

import matplotlib.pyplot as plt
import psutil
from psutil import cpu_percent

file = open("data.txt", "r")
mem = open("memory.txt", "r")
a = []
for i in file:
    a.append(i.strip()[24:30])
c = []
for i in a[1:-1]:
    c.append(float(i.replace(" ", "")))
#print(c)

m =[]
for i in mem:
    m.append(i.strip()[36:41])
memory = []

for i in m[1:-1]:
    memory.append(float(i))
print(memory)

plt.plot(c, label="CPU")
plt.title("Performance measure")
plt.plot(memory, label="Memory")
plt.axvline(x=15, linestyle="dashed", color="red", ymax=0.97, label="start attack")
plt.axvline(x=25, linestyle="dashed", color="purple",ymax=0.97, label="network tracking")
plt.axvline(x=85, linestyle="dashed", color="green", ymax=0.97, label="attack killed")
plt.xlabel("seconds")
plt.legend()
plt.ylabel("CPU usage of all 4 Cores")
plt.savefig("plotCPUUsage.png")