import sys as sus
x=input()
l=list(x)
#a=['a', 'b', 'c', 'd',  'f', 'g', 'i', 'j', 'k', 'm', 'n', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
a=['h','e','l','l','o']
z=[]
for i in l:
    if i in a:z.append(i)
#print(z)
#k=[]
#for i in range(len(z)):
 #   if z[i-1]!=z[i]:
  #      k.append(z[i]) 
#print(k)
#n=len(k)
for i in z:
    if len(a)>0:
        if i==a[0]:a.remove(a[0])
    #    print(i)
print('YES' if len(a)==0 else 'NO')

#import sys as sus
#x=input()
#a=['h','e','l','l','o']
#y=list(x)
#b=[]
#for i in y:
 #   if i=='h':b=[]
  #  if i in a:
   #     if i not in b:
    #        b.append(i)
    # o=''.join(i for i in b)
    #if o=='helo':
     #   print('YES')
      #  sus.exit()
#print(b)
# print('NO')        
#b=[i for i in y if i in a not in b]
#print(b)
#o=''.join(i for i in b)
#print('YES' if o=='helo' else 'NO')
 
