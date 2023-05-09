from math import floor
t=int(input())
for i in range(t):
    n,s,r=[int(x) for x in input().split()]
    z=s-r
    a=[0]*n
    a[-1]=z
    #a[-2]=s-sum(a)+1
    #print(a)
    f=0
    #or i in range(len(a)-1):
    #    a[i]=floor((r)/(n-1))
    #    f=f+floor((r)/(n-1))
    #a[1]=a[1]+r-f
    #for i in range(len(a)-1):
    while r>0:
        for i in range(len(a)-1):
            a[i]=a[i]+1
            r=r-1
            if r==0:
                break
            
            
        
    
        
    for i in range(len(a)):
        print(a[i],end='')
        print(' ',end='')
    print('')
    