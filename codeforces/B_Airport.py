f=[]
n,m=[int(x) for x in input().split()]
f=[int(x) for x in input().split()]
z=[i for i in f]
costumax=0
for i in range(n):
    #for i in f:
    #    if i<=0:f.remove(i)
    x=sorted(f,reverse=True)
    #print(x)
    costumax=costumax+x[0]
    f[f.index(max(f))]=max(f)-1
costumin=0
for i in range(n):
    for i in z:
        if i<=0:z.remove(i)
    x=sorted(z)
    #print(x)
    costumin=costumin+x[0]
    z[z.index(min(z))]=min(z)-1 
  
print(costumax,costumin)