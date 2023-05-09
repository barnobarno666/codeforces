def fuck(nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        bam=-1
        dan=-2
        a=1
        maxx=min(nums)
        z=sorted(nums,reverse=True)
        if z==nums:
            a=0
            #f=list(sorted(nums))
            nums.sort()
            
        while True and a==1:
            print(bam,dan,nums)
            if nums[bam]==maxx:
                bam=bam-1
                dan=bam-1
            
            
            elif nums[dan]>nums[bam]:
                #bam=bam-1
                maxx=nums[dan]
                dan=dan-1
                    
            else:
                if dan-bam!=-1:nums[dan],nums[dan+1],nums[bam]=nums[bam],nums[dan],nums[dan+1]
                else:nums[dan],nums[bam]=nums[bam],nums[dan]
                break
        return nums
            

#nums=[2,3,1]
#nums =[2,5,2,1]
#Output
#[3,1,2]
#Expected
#[2,1,3]"""

#nums =[1,1,5]

print(fuck(nums))
