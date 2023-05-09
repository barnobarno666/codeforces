from sys import exit
n=int(input())
f=[int(x) for x in input().split()]
z=sorted(f)
if len(f)==1:
    print('YES')
    exit()
if z[-1]!=z[0]:
    print('YES')
    exit()
print('NO')