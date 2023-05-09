import math

def num_gen(n, j, zero_count):
    sux = 0
    k = 1
    for i in range(n, 0, -1):
        sux = 5 * pow(10, i) + sux
    sux = sux // 10
    while k <= zero_count:
        k = k + 1
        sux = sux * 10
    return sux

n = int(input())
a = [int(x) for x in input().split()]
bara = [0 for _ in range(n)]
zero_count = a.count(0)
summ = 0
k = 0
for i in range(n):
    summ += a[i]
    k = i
    if summ % 9 == 0 and summ != 0:
        if zero_count != 0:
            bara[i] = k
        if zero_count == 0:
            bara[i] = k + 1
bara.sort()
if bara[-1] != 0:
    f = bara[-1]
    print(num_gen(f, n, zero_count))
else:
    if 0 in a:
        print(0)
    else:
        print(-1)
