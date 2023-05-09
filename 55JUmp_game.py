def fuck(nums):
        #while i < len(nums):
        f=nums.count(0)
        if f==0:
            return True
        #j=0
        """"
        non greedy approch 
        #for i in range(f):
        #    j=f.index(0)
        #    for k in range(j):
        #        if f[k]-j>0:
        #            break"""
        index=0
        f=[[nums[i],i] for i in range(len(nums))]
        f=f[2:]
        print(f)
        return f[0].index(1)
        maxx_count=nums[0]
        x=len(nums)-1
        while True:
            """#greedy approch, first e start, then otar range e sort korbe, then maximum e jabe,eivabe 
            #othoba ota theke ager diff dekhbe, then new te jabe
            #eivabe hobar kotha"""
           
            maxx=max(nums[index+1:index+1+nums[index]])
            print(nums,nums[index:],index)
            nums=nums[index+1:]
            index=nums.index(maxx)
            print(nums,index,nums[index])
            #print(maxx_count)
            if index==len(nums)-1 or maxx_count>=x:
                return True
            elif maxx==0:
                return False 
            maxx_count=maxx
        return True  
nums=[3,2,1,0,4]
nums=[1,0,2]
nums=[2,0,0]
nums=[2,5,0,0]
nums=[1,2,1,0,4]
nums=[1,1,0,1]
print(fuck(nums))