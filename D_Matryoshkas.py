# t=int(input())
# for i in range(t):
#     n=int(input())
#     f=[int(x) for x in input().split()]
#     #ans=[f.count(i) for i in f]
#     #for i f:
#     #    ans.append(f)
#     print(max(ans))
t=int(input())
for i in range(t):
    n=int(input())
    ans=1
    f=[int(x) for x in input().split()]
    f.sort()
    #print(f)
    z=[]
    ansd=[f.count(i) for i in f]
    #ans=ans+max(ansd)-1
    #for i in f:
        #if f.count(value)
    for i in range(len(f)):
        if f[i]-f[i-1]>1  :
            #if f[i+1] not in z:
            ans=ans+1
            if  f.count(f[i])>f.count(f[i-1]):
                ans=ans+f.count(f[i-1])-f.count(f[i])
                
            # z.append(f[i+1])
        #else:
            
            
    ansd=[f.count(i) for i in f]
    ans=ans+max(ansd)-1
    print(ans)
        
        