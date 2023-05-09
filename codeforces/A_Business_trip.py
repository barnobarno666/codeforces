n=int(input())
a=[int(x) for x in input().split()]
b=sorted(a,reverse=True)
#print(b)
i=0
while i<12:
     if n<=0:break
     n=n-b[i]
     i=i+1

print(i if sum(a)>=n else -1)


