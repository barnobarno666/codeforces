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
        middle_true=middle
        middle_truest=middle
        for _ in range(10): 
            zz=False
            if z[bam]!=z[dan] and z[middle]!=z[dan] and z[bam]!=z[middle] and z[dan]+z[bam]+z[middle]==0:
                    f.append([z[dan],z[bam],z[middle]])
                    zz=True
            #for _ in range(middle,dan):
            #    if middle==dan:break
            #    if z[dan]+z[bam]+z[middle]>0:break
            if z[dan]+z[bam]+z[middle]>0:
                dan=dan-1
            for i in range(middle,dan):
                middle=i
                if middle==dan:break
                if z[dan]+z[bam]+z[middle]>0:break
                if z[bam]!=z[dan] and z[middle]!=z[dan] and z[bam]!=z[middle] and z[dan]+z[bam]+z[middle]==0:
                    f.append([z[dan],z[bam],z[middle]])
            
            if z[dan]+z[bam]+z[middle]<0:
                bam=bam+1
            if bam==dan-2:
                break
            
                    #zz=True
                #middle=middle+1
            #if z[dan]+z[bam]+z[middle]>0:
               # =dan-1
            
            
                    
            i
            
            
        #if bam==dan or dan==middle:
        #    return f
        return z,middle,f
nums = [-1,0,1,2,-1,-4]
print(fuck(nums)) 