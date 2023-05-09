from math import ceil
from sys import  exit
x=input()
y=list(x)
j=0
#if len(y)%2==1:z=y[ceil(len(y)/2)-1]
#print(z)
if len(y)%2==1 :
    l=list(reversed(y[ceil(len(y)/2):]))
    #print(z,y[:ceil(len(y)/2)-1])
    if l==y[:ceil(len(y)/2)-1]:
        print('First')
        exit()

#print(len(y))
if len(y)%2==1:
    y.remove(z)
   # j=j+1
#print(len(y))
for i in y:
    if y.count(i)%2!=0 and y.index(i)!=ceil(len(y)/2)-1:
        del y[y.index(i)]
        j=j+1
        #if len(y)%2==1:
        #    z=y[ceil(len(y)/2)-1]
        #    y.remove(z)
            #j=j+1
    elif y.index(i)!=ceil(len(y)/2)-1 and y.count(i)>1 and y.count(i)%2!=0 :
        a=list(reversed(y))
        del y[len(y)-a.index(i)-1]
        j=j+1
d=[1,2,3,4,5,6,7,8,9,10,11]


#print(''.join(i for i in y))
print('First' if j%2==0 else 'Second')