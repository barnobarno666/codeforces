n,a,b=[int(x) for x in input().split()]
#a=n[1:]
#n=n[0]
i=0
while b >= 0:
    if (n-b-1) >= a:
        i=i+1  
        a=a+1     

    b=b-1
   
    
print(i)


