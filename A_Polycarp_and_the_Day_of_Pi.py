a=['3', '1', '4', '1', '5', '9', '2', '6', '5', '3', '5', '8', '9', '7', '9', '3', '2', '3', '8', '4', '6', '2', '6', '4', '3', '3', '8', '3', '2', '7', '9']
t=int(input())
for i in range(t):
    k=0
    f=int(input())
    z=list(str(f))
    for j in range(len(z)):
        if z[j]!=a[j]:
            break
        k=k+1
    print(k)
