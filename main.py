import matplotlib.pyplot as plt

from Parser import Parser

file = open("data.txt", "r")
mem = open("memory.txt", "r")
a = []
for i in file:
    a.append(i.strip()[74:80])
c = []
for i in a[1:-1]:
    c.append(round(100 - float(i.replace(" ", "")), 2))
print(c)

m = []
for i in mem:
    m.append(i.strip()[36:41])

me = []
for i in m[1:-1]:
    me.append(float(i))
print(me)
s = 0
s3 = 0
cou3 = 0
for i in me[30:90]:
    cou3 += 1
    s3 += i
cou = 0
for i in me[:30]:
    s += i
    cou += 1
for i in me[90:]:
    s += i
    cou += 1

avgusmemory = s / cou
print(avgusmemory)
print(s3 / cou3)

upxmr, downxmr, upsensor, downsensor = Parser("nethogs.txt").parse()

avg = 42.75
# plt.plot(memory, label="Sent KB/s")
plt.title("Network usage during Reconnaissance attack without Firewall")
# plt.plot(upxmr, label="XMRig upload KB/s")
# plt.plot(downxmr, label="XMRig download KB/s")
plt.axvline(x=20, linestyle="dashed", color="red", ymax=0.97, label="start Reconnaissance attack")
plt.axvline(x=63.10, linestyle="dashed", color="green", ymax=0.97, label="finished Reconnaissance attack")

plt.plot(upsensor, label="Upload KB/s")
plt.plot(downsensor, label="Download KB/s")
# plt.plot(downsensor, label="Download KB/s")
# plt.axvline(x=50, linestyle="dashed", color="black",ymax=0.97, label="delay")
# plt.axvline(x=21.9, linestyle="dashed", color="green",ymax=0.97, label="finished Arp-Scan attack")
# plt.axvline(x=0, linestyle="dashed", color="red", ymax=0.97, label="Start Cryptojacker")
# plt.axvline(x=0, linestyle="dashed", color="green", ymax=0.97, label="Start Cryptojacker")
# plt.axvline(x=80, linestyle="dashed", color="red", ymax=0.97, label="Kill Cryptojacker")
# plt.axvline(x=95, linestyle="dashed", color="purple", ymax=0.97, label="Setup Firewall")
# plt.axvline(x=100, linestyle="dashed", color="orange", ymax=0.97, label="Start Cryptojacker")
# plt.axvline(x=64, linestyle="dashed", color="black", ymax=0.97, label="Finished Reconnaissance attack")
# plt.plot(upsensor, label="Total Upload KB/s")
# plt.plot(downsensor, label="Total download KB/s")


# plt.axhline(y=avg, linestyle="dashed", color="orange", xmin=0.03, xmax=0.97, label=f"Mean {round(avg,2)}")

# plt.plot(downsensor, label="Total Download KB/s")
# plt.plot(upsensor, label="Network download KB/s")
# plt.bar([1,2,3,4,5,6,7,8,9,10],p)
plt.xlabel("Seconds")
plt.legend()
plt.ylabel("Total Network usage in KB/s")
plt.savefig("network15.png")
