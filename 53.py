def solve(nums):
    def summ(nums,bam,dan):
        summ2=0
        for i in range(bam,dan+1):
            summ2=summ2+nums[i]
        return summ2
    """maxx=0
    if len(n)==1:
        return n[0]
    if len(n)==0:
        return 0
    else:
        maxx=max(solve(n[1:], maxx),solve(n[0:], maxx))
    return maxx"""
    bam=0
    dan=len(nums)-1
    f=[]
    while True:
        if bam==dan:
            break
        else:
            f.append(summ(nums,bam, dan))
            print(bam,dan)
        if nums[bam+1]>nums[dan-1]:
            bam=bam+1
        elif nums[bam+1]<nums[dan-1]:
            dan=dan-1
        else:
            if summ(nums,bam+1,dan)>summ(nums,bam,dan-1):
                bam=bam+1
            else:
                dan=dan-1
            
            
    return f
            
    
    
    
nums = [-2,1,-3,4,-1,2,1,-5,4]
#nums=[5,4,-1,7,8]
print(solve(nums))