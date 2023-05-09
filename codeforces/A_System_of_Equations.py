from math import sqrt ,ceil,floor
m,n=[int(x) for x in input().split()]
x=ceil(sqrt(m+n))
k=0
for i in range(0,x):
    for j in range(i,x):
        #print(i,j)
        #if i**2+i+j**2+j== (m+n):
        if (i**2+j==n and j**2+i==m):
            k=k+1
            print(i,j)
        elif (i**2+j==m and j**2+i==n):
            k=k+1

        #print(i,j)
print(floor(k))