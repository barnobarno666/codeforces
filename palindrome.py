from math import floor
def isPalindrome(s):
        x=[i.lower() for i in s]
        s=s.lower()
        #return x
        a=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0']
        for i in s:
            if i not in a:
                x.remove(i)
        #return x
        for i in x:
            if i==' ':
                del x[x.index(i)]
        for i in x:
            if i=='':
                del x[x.index(i)]
        #return x
        for i in range(floor(len(x)/2)):
            if x[i]!=x[len(x)-1-i]:
               return False
                 
        return True
s="......a....."
print(isPalindrome(s))