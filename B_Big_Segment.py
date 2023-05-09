from sys import exit
n=int(input())
f=[]
hi=[]
lo=[]
for i in range(n):
    k,l=[int(x) for x in input().split()]
    f.append([k,l])
    hi=hi+[k]
    lo=lo+[l]
hii=min(hi)
loo=max(lo)
for i in range(len(f)):
    if f[i][0]==hii and f[i][1]==loo:
        print(i+1)
        exit()
for i in range(len(f)):
    if f[i][1]==hii and f[i][0]==loo:
        print(i+1)
        exit()
print(-1)