import math
def fuck(nums):
        z=sorted(nums)
        bam=0
        dan=len(z)-1
        middle=0
        f=[]
       
        for i in range(len(z)):
            if z[i]!=z[0]:
                middle=i
                break
        if bam==dan or dan==middle:
            return f
        if z[dan]+z[bam]+z[middle]>0:
            while z[dan]+z[bam]+z[middle]>0:
                dan=dan-1
        while True:
            if z[dan]==z[bam]:break
            midlesta=math.floor(len(z)/2)
            #if z[bam]!=z[dan] and z[middle]!=z[dan] and z[bam]!=z[middle] and z[dan]+z[bam]+z[middle]==0:
            #        f.append([z[dan],z[bam],z[middle]]
            while True:
                print(bam,dan,midlesta)
                if z[dan]+z[bam]+z[midlesta]<0 and z[dan]+z[bam]+z[midlesta+1]>0:break
                if z[midlesta]==z[bam] or z[midlesta]==z[dan]:break
                if z[dan]+z[bam]+z[midlesta]==0:
                    f.append([z[dan],z[bam],z[midlesta]])
                if z[dan]+z[bam]+z[midlesta]>0:
                    midlesta=midlesta-1
                elif z[dan]+z[bam]+z[midlesta]<0:
                    midlesta=midlesta+1
                
                
            if z[dan]+z[bam]+z[middle]<0:
                bam=bam+1
            if  z[dan]+z[bam]+z[middle]>0:
                dan=dan-1
            print(f)
        return f
                            
nums = [-1,0,1,2,-1,-4]
print(fuck(nums))
[-4,-1,-1,0,1,2]
                