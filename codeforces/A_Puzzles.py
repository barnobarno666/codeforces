n,m=[int(x) for x in input().split()]
f=[]
#for i in range(m):
f=[int(x) for x in input().split()]
f.sort(reverse=True)
a=[0]*(len(f)-7)
for i in range(len(f)-n):
    a.append(f[i]-f[i+n-1])

#print(f)
#print(a)
if len(a)>0:print(min(a))
else:print(0)