from sys import exit
n,m=[int(x) for x in input().split()]
n_1=[int(x) for x in input().split()]
m_2=[int(x) for x in input().split()]
nmin=min(n_1)
nmax=max(n_1)
mlow=min(m_2)
if mlow < nmax:
    print(-1)
    exit()
f=[]
for i in range(nmax,mlow):
    if i >= nmin *2:
        f.append(i)
if len(f)==0:
    print(-1)
    exit()
print(min(f))

