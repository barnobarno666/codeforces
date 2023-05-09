from sys import exit
a=list(input())
b=list(input())
if len(a)!=len(b):
    print('NO')
    exit()

for i in a:
    if i not in b:
        print('NO')
        exit()
r=0
for i in range(len(a)):
    if a[i]!=b[i]:
        r=r+1
if r>2:
    print('NO')
    exit()
aa=sorted(a)
bb=sorted(b)
if r<=2 and a.count(aa[0])==b.count(aa[0]):
    print('YES')
    exit()
print('NO')
