def fuck(s):
    nums=list(s)
    if len(s)==0:
        return 0
    a=[]
    score=[]
    j=0
    #if nums.count(nums[1])==len(nums):
        
    #    return 1
    
    for i in range(len(nums)):
        
        #print(a,nums[i],j)
        score.append(len(a))
        if nums[i] not in a:
            a.append(nums[i])
            #print('fuck')
            j=j+1
            score.append(len(a))
            #if i==len(nums)-1:score.append(j)
        elif nums[i] in a:
            #print('suck')
            score.append(len(a))
            a=a[a.index(nums[i])+1:]
            a.append(nums[i])
            j=len(a)
        
    return max(score)

s = "bbbbbbbbb"
#s="pwwkew"
#s="aab"
#s="dvdf"
print(fuck(s))
    

            
        