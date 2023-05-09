from math import ceil
from sys import exit
# a=[1,2,3,4,5,6,7,3,0]
# y=list(reversed(a))
# #print(a[ceil(len(a)/2):])
# print(len(a))
# print(a.index(7),y.index(7))
def cunt(a,b):
    return sum(x.count(b) for x in a)
def fck(f,d):
    for i in range(len(f)):
        if f[i][1]==d+1:
            return 1
    return 0
def ispolindrome(y):
    
    l=list(reversed(y[ceil(len(y)/2):]))
        #print(z,y[:ceil(len(y)/2)-1])
    #print(l,y[:ceil(len(y)/2)-1])
    if l==list(y[:ceil(len(y)/2)-1]) or l==list(y[:ceil(len(y)/2)]) :
            #print('First')
            return 1
    return 0
#print(ispolindrome(['a','b','a']))
x=input()
y=[[x[i],i] for i in range(len(x))]
z=list(x)
#print(y)
if ispolindrome(x)==1:
    print('First')
    exit()
f=[]
#f.append([])
j=0
#print(y[2][0])
#print(cunt(y, 'x'))
k=0
for i in range(len(y)):
    x=y[i][0]
    p=x
    #print(y[i][0],i)
    #print(p)
    if cunt(y, p)%2!=0:
        #print(cunt(y, p),p) 
        f.append([y[i][0],y[i][1]])
        #f[i].append(y[i][1])
        #print(i)
        y[i].remove(p)
        y[i].remove(i)
        #y.remove([])
        #k=k+1
#print(len(y),y)
m=y.count([])
for i in range(m):
    y.remove([])

d=y[round((len(y)/2)-1)][1]
#print(d)




#print(len(y),y)
#print(' '.join(i for i in f))
print(fck(f, d))
if fck(f, d)==1:
    j=len(f)-1
else:
    j=len(f)
#if len(y)%2==0:j=len(f)-1
#if len(y)&2!=0:j=len(f)
#print(len(f))
print('First' if j%2==0 else 'Second')
#while ispolindrome(y)!=1:
#    for i in y:
#        #if len(y)%2==0:x=y[ceil(len(y)/2)]
#        if y.count(i)%2