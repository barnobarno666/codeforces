n,m=[int(x) for x in input().split()]
f=[[]]*n
for i in range(n):   
    f[i]=list(input()) 
#upor nicher duita nije fillup korbo
for i in range(1,m):
    if f[0][0]=='.':f[0][0]='B'
    if f[0][i]=='.' and f[0][i-1]!='B':
        f[0][i]='B'
for i in range(1,m):
    if f[0][0]=='.':f[0][0]='W'
    if f[0][i]=='.' and f[0][i-1]!='W':
        f[0][i]='W'
for i in range(1,m):
    if f[n-1][0]=='.':f[n-1][0]='W'
    if f[n-1][i]=='.' and f[n-1][i-1]!='W':
        f[n-1][i]='W'
for i in range(1,m):
    if f[n-1][0]=='.':f[n-1][0]='B'
    if f[n-1][i]=='.' and f[n-1][i-1]!='B':
        f[n-1][i]='B'


for i in range(1,n-1):
    for i in range(m):
        if f[n-1][m] !='B' and f[n+1][m] !='B' and f[n][m-1] !='B'  :
            
            f[n][m]='B'

for i in range(n):
    print(''.join(i for i in f[i]))

#for i in range(stop)
#print(f)
