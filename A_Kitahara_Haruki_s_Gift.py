from sys import exit
n=int(input())
f=[int(x) for x in input().split()]
#if sum(f)%200 ==0:
#    print('YES')
z=sorted(f)
if len(f)==1:
    print('NO')
    exit()
#for i in range(len(f)):
#    if z[-1]==200 and z[0]==100 and z[1]==100:
#        z.remove(200)
#        z.remove(100)
#        z.remove(100)
o=z.count(200)
sh=z.count(100)
#print(o,sh) 
if o%2==0 and sh%2==0 :
    print('YES')
    exit()
elif  o%2!=0 and sh%2==0 and sh > 0:
    print('YES')
    exit()


print('NO')
#print(z)