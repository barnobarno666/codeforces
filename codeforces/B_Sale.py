n,m=[int(x) for x in input().split()]
b=[int(x) for x in input().split()]
a=sorted(b)
#print(a[:m])
print(abs(sum([i for i in a[:m] if i<0])))