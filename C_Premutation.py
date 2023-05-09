t=int(input())
for i in range(t):
    f=[]
    n=int(input())
    for i in range(n):
        z=[int(x) for x in input().split()]
        f.append(z)
    ans=[]
    
    
    
    for i in range(n-1):
        sub=[]
        for j in range(n):
            sub.append(f[j][i])
        #print(sub)
        sub.sort()
        #print(ans,sub)
        if sub.count(sub[-1])>sub.count(sub[0]):
            if sub[-1] not in ans:
                ans.append(sub[-1])
            if sub[0] not in ans:ans.append(sub[0])
        elif sub.count(sub[-1])<sub.count(sub[0]):
            if sub[0] not in ans:ans.append(sub[0])
            if sub[-1] not in ans:ans.append(sub[-1])
        else:
            if sub[0] not in ans:ans.append(sub[0])
            if sub[-1] not in ans:ans.append(sub[-1])
        
        
        
        #j=j+2
        
    for i in range(n):
        print(ans[i],end=' ')
    print('')
    
        
        
        