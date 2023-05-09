def fuck(num):
    a={1:'I',5:'V',10:'X',50:'L',100:'C',500:'D',1000:'M'}
    key=0
    f=0
    z=0
    k=[]
    numm=0
    kk=[]
    while True:

        if num==0 or num <0 :
            break
        for i in a:
            #print(a[i])
            if num% i==num:
                #print(i)
                #k=[k[-1]]
                break
            elif num%i>=0:
                z=a[i]
                numm=i
                if i<=num:k.append(z)

        kk.append(z)
        if len(kk)>=4:
            if kk[-4:-1]+[kk[-1]]==['I','I','I','I']:
                del kk[-1]
                del kk[-1]
                del kk[-1]
                del kk[-1]
                kk.append('I')
                kk.append('V')
            elif kk[-4:-1]+[kk[-1]]==['V','V','V','V']:
                del kk[-1]
                del kk[-1]
                del kk[-1]
                del kk[-1]
                kk.append('V')
                kk.append('X')
            elif kk[-4:-1]+[kk[-1]]==['L','L','L','L']:
                del kk[-1]
                del kk[-1]
                del kk[-1]
                del kk[-1]
                kk.append('L')
                kk.append('C')
                
        
        #print(z)
        #f=[i for i in a if a[i]==z]
        #if len(f)>0:f=f[0]
        #else:f=0
        num=num-numm
        #print(z)
        #z.append()
                
        #f=f[1:]
            
        #print(a[i]) 
      
    return ''.join(i for i in kk)
    #return a[5]
print(fuck(58))
