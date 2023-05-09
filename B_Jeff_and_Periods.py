def fncchek(lister):
    if len(lister)==1:return 0
    z= lister[1]-lister[0]
    for i in range(len(lister)-1):
        if lister[i+1] - lister[i]!=z:
            return 0
    return z
n=int(input())
f=[int(x) for x in input().split()]
z=[i for i in f]
m=[[f[i],i] for i in range(len(f))]
final=[]
l=sorted(m)
answ=[]
b=[0]
for i in range(len(l)):
    nn=[]
    if l[i][0] !=b[-1]:
        for j in range(i,len(l)):
            if l[j][0]!=l[i][0]:break
            if l[j][0]==l[i][0]:
                nn.append(l[j][1])
        o=fncchek(nn)
        if o!=0:
            answ.append([l[i][0],o])
    b.append(l[i][0])
for i in f:
    if f.count(i)==1:
        answ.append([i,0])
fasnser=sorted(answ)
print(len(answ))
for i in range(len(answ)):
    print(fasnser[i][0],fasnser[i][1])
