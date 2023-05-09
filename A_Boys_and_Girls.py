n,m=[int(x) for x in input().split()]
f=[]
if n>=m:
    f.append('B')
    n=n-1
elif m>n:
    f.append('G')
    m=m-1
while n>0 or m>0:
    if f[0]=='B':
        if m>0:
            f.append('G')
            m=m-1
        if n>0:
            f.append('B')
            n=n-1
    elif f[0]=='G':
        if n>0:
            f.append('B')
            n=n-1
        if m>0:
            f.append('G')
            m=m-1
for i in f:
    print(i,end='')     