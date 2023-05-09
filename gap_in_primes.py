def gap(g, m, n):
    #a=[1,2]
    kk=[]
    
    a=[i for i in range(m,n+1)]
    b=[]
    #return a
    ll=0
    for i in range(m,n+1):
        ll=0
        for j in range(2,m):
            if i%j==0:
                ll=1

        if ll==0:b.append(i)
    return b
              

print(gap(1, 10, 100))