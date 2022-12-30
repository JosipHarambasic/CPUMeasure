import os
import time

import matplotlib.pyplot as plt
import psutil
from psutil import cpu_percent


cpu_usage = []
memory_usage = []
while True:
    if len(cpu_usage) > 100:
        break
    cpu_usage.append(cpu_percent(0.1)/100)
    memory_usage.append(psutil.virtual_memory().percent/100)
    time.sleep(0.1)

plt.plot(cpu_usage, label="CPU Usage")
plt.plot(memory_usage, label="Memory Usage")
plt.ylabel('Percentage %')
plt.xlabel('Timestamps in 0.1s steps')
plt.legend()

# save
strFile = "plotCPUandMemoryUsage.png"
if os.path.isfile(strFile):
    os.remove(strFile)
plt.savefig("plotCPUandMemoryUsage")