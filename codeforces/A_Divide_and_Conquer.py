n,m=[int(x) for x in input().split()]
f=[]
#for i in range(m):
f=[int(x) for x in input().split()]
f.sort(reverse=True)
a=[]
i=1
while i<len(f)-n+1 :
    a.append(abs(f[-n-i+2]-f[-i]))
    i=i+n
print(f)
print(a)
if len(a)>0:print(min(a))
else:print(0)