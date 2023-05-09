import sys as sus
x=input()
f=[int(i) for i in x]
#print(f)
if len(f)<7:
    print('NO')
    sus.exit()
i=0
a=[]
#print(i+7)
while i<len(f)-7+1:
    k=i+7
    a.append(sum(f[i:k]))
    i=i+1

#a=[0]*(len(f)-7)
#for j in range(len(f)-7-1):
  #  for i in range(j,j+6):
   #     a[j]=a[j]+f[j+i]
if 0 in a or 7 in a:print('YES')
else:print('NO')