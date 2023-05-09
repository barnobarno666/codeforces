from sys import exit
y,k,n=[int(x) for x in input().split()]
f=[]
x=0
#print(n-k,n-y)
if n-k> n-y :
    for i in range(1,n-y):
        if (y+i)%k==0:
            f.append(i)
            if len(f)==2:break
elif n-k <= n-y :
    #print('-e3e')
    i=n-y
    while i >= 1:
        #print(i)
        if (y+i)%k==0:
            f.append(i)
            if len(f)==2:break
        if y+i+k> n :break
        i=i-1
    
if len(f)==0:
    print(-1)
    exit()
x=abs(f[-1]-f[0])
j=f[0]
if n-k >n-y:
    while j<=(n-y):
        print(j,end=' ')
        j=j+x
elif n-k <= n-y :
     while j<=(n-y):
        print(j,end=' ')
        j=j-x
