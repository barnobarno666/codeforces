def fck(height):
    f=[]
    for i in range(len(height)):
            f.append([height[i],i])
    k=sorted(f,reverse=True)
    p=[i for i in k]
        #for i in range(len(p)-1):
            
    maxx=0
    z=[]
    for i in range(len(k)-1):
            #if p[i][0]==p[i+1][0] and p[i][1]>p[i+1][1]:
            #    p[i],p[i+1]=p[i+1],p[i]
            #z.append(abs((min(k[i+1][0],k[i][0])*(k[i+1][1]-k[i][1]))))
            #z.append(abs((min(p[i+1][0],p[i][0])*(p[i+1][1]-p[i][1]))))
            #for j in range(i,len(k)-1):
            #    if abs(p[j][1]-
        maxx=p[i+1][1]-p[i][1]
        for j in range(i,len(k)-1):
                if abs(p[j][1]-p[i][1])>=maxx:
                    z.append((p[j][0])*abs(p[j][1]-p[i][1]))
        #return p 
    return z
    if len(z)==1:
        return height[0]*height[1]
        #return k[0][0]*k[1][0]
    return (max(z))


height=[1,2,3,4,5,6,7,8,9,10]
height=[1,1,9]
print(fck(height))
print(height[0::5])