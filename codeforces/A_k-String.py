import sys as sus
n=int(input())
s=input()
x=list(s)
sorted(x)
#print(y)
a=[]
if len(x)%n!=0:
    print(-1)
    sus.exit()
for i in x:
    if i not in a:
        a.append(i)
#print(a,len(a))
#if len(a)>n:
 #   print(-1)
  #  sus.exit()
j=[x.count(i) for i in a]
j.sort()
if j[0]!=j[-1]:
    print(-1)
    sus.exit()
a=a*n
l=''.join(str(x) for x in a)
print(l)

