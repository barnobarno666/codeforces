from sys import exit
#def isbeauty(z):
    #for i in range(len(z)):
t=int(input())
for i in range(t):
    p=1
    n=int(input())
    f=[int(x) for x in input().split()]
    z=sorted(f,reverse=True)
    if z==f:
        p=0
        print('NO')
    
    if z[0]==z[1] and len(z)== 2 and p!=0:
        print('NO')
        #break
    
    if len(z)!=2 and p==1:
        for i in range(len(z)):
            if sum(z[:i])==z[i]:
                z[i],z[-1]=z[-1],z[i]
    if z[0]!=z[1] and p==1:
        print('YES') 
        #print(z)       
        for i in z:
            print(i,end=' ')
        print('')
        