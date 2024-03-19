from math import log
k = 1
s = 0
m = 1
for i in range(10**10):
    if i % 2 == 0:
        s += 4 / k
    else:
        s -= 4 / k
    k += 2
    if i % m == 0:
        m = 1
        while int((4/k)*(m)) == 0:
            m *= 10
        print(str(round(s, int(log(m, 10))))[:-2])
