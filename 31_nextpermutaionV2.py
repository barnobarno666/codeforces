def fuck(nums):
    dan=-2
    bam=-1
    a=1
    z=sorted(nums,reverse=True)
    if z==nums:
            a=0
            #f=list(sorted(nums))
            nums.sort()
            return nums
    while True and a==1: 
        #print(bam,dan)
        if nums[bam]==min(nums) or nums[bam]==nums[dan]:
            #return nums.sort
            bam=bam-1
            dan=bam-1
        #print(bam,dan)
        elif nums[dan]>=nums[bam]:
                #bam=bam-1
                #maxx=nums[dan]
            dan=dan-1       
        elif nums[dan]<nums[bam]:
            nums[bam],nums[dan]=nums[dan],nums[bam]
            
            #print(nums[:dan+1],nums[dan+1:],nums)
            z=nums[dan+1:]
            nums=nums[:dan+1]+list(sorted(z,reverse=False))
            break
        #else:
            #dan=dan-1
    
    print(nums)

#nums=[2,3,1]
nums =[2,5,2,1]
nums =[2,5,2,1]
#Output
#[3,1,2]
#Expected
#[2,1,3]"""
#nums =[1,3,2]

#nums =[1,1,5]
#nums = [3,2,1]
print(fuck(nums))
            
            
        
            