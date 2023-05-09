f=[]
x=int(input())
for i in range(x):
    f.append(input())

f.sort()
#print(f)
print(f[0] if f.count(f[0]) > f.count(f[-1]) else f[-1] )