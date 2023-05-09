def isValid(s):
        def ulta(x):
            if x==')':
                return '('
            elif x==']':
                return '['
            elif x== '}':
                return '{'
        if len(s)%2!=0:
            return False
        middle = int(len(s)/2)
        bam=middle-1
        dan=middle
        z=list(s)
        print(z)
        
        for i in range(middle):
            #print(bam,dan)
            if dan>=2*middle:
                break 
            if z[bam]!=ulta(z[dan]):
                
                print(z[bam],ulta(z[dan]))
                idd=False 
            bam=bam-1
            dan=dan+1
        for x in range(len(z)):
            if z[x]==')':
                if z '('
            elif x==']':
                return '['
            elif x== '}':
                return '{'
        if len(s)%2!=0:
            return False
        
        
        return True
s = "()[]{}"
print(isValid(s))
