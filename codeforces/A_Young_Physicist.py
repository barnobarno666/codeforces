n=int(input())
p=[[0,0,0]]*n
x,y,z=0,0,0
for i in range(n):
    p[i]=[int(x) for x in input().split()]
for i in range(n):
    x=p[i][0]+x
    y=p[i][1]+y
    z=p[i][2]+z

print('YES' if x==0 and y==0 and z==0 else 'NO') 