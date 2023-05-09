x=input()
b=list(x.lower())
f=['.'+i for i in b if i not in a]
n=''
for i in range(len(f)):
    n=n+f[i]
print(n) 