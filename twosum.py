#print(101%1000)
a={1:'I',5:'V',10:'X',50:'L',100:'C',500:'D',1000:'M'}
f=[i for i in a if a[i]=='L']
f=f[0]
#print(f)
a=[1,2,3,4,5,6,7,8,9,10]
z=a[a.index(8):]
print(z)
#print(a[-4:-1]+[a[-1]])
##a=a[:2]+list(a[2:]).sort(reverse=True)
print(a[2:],a[:2])

a=a[:2]+list(sorted(a[2:],reverse=True))
print(a)
