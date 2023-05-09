def lexo(a,b,c):
    f=[]
    #for i in range(len(s)):
    f.append(a)
    f.append(c)
    f.append(b)
    z=sorted(f)
    if f[0]==b or f[-1]==b:
        return f,True
    return False
        
print(lexo('ab', 'b', 'a'))   
    
    
#t=int(input())
#for i in range(t):
    #f=input()
    
    
    