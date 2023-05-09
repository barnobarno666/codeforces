x=input()
y=x.split('WUB')
#print(y)
o='0'.join(i for i in y)
for i in range(2,100):
    o=o.replace('0'*i, ' ')
o=o.replace('0', ' ')
#for i in range(len(x)):
 #   if y[i]+y[i+1]+y[i+2]=='WUB':
print(o)
#WE ARE THE CHAMPIONS MY FRIEND
#WE ARE  THE CHAMPIONS MY FRIEND