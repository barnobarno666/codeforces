def isValid(s):
    def ulta(x):
            if x==')':
                return '('
            elif x==']':
                return '['
            elif x== '}':
                return '{'
            else:
                return x
    ultano=['}',')',']']
    score={'(':0,'[':0,'{':0}
    #s['(']=s['(']+1
    #print(s['(']+1)
    for i in range(len(s)):
        if s[i] in ultano :
            score[ulta(s[i])]=score[ulta(s[i])]-1
        else :
             score[ulta(s[i])]=score[ulta(s[i])]+1
        if s[i] in ultano and s[i-1] not in ultano:
            if ulta(s[i])!=s[i-1]:
                print(ulta(s[i]),s[i-1],s[i])
                return False

    if s['(']+s['}']+s['[']!=0:
        return False
    return True
               
S="{[]}"

print(isValid(S))