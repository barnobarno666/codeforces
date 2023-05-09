def fuck(nums):
        z=sorted(nums)
        bam=0
        bamTrue=bam
        f=[]
        dan=len(z)-1
        dantrue=dan
        middle=0
        
       
        for i in range(len(z)):
            if z[i]!=z[0]:
                middle=i
        #if bam==dan or dan==middle:
        #    return f
        middle_true=middle
        middle_truest=middle
        while True:
            print( [bam,dan,middle])
            xp=1
            pp=1
            zz=False
            
            if bam and dan and middle<len(z):
                if z[bam]!=z[dan] and z[middle]!=z[dan] and z[bam]!=z[middle] and z[dan]+z[bam]+z[middle]==0:
                    f.append([z[dan],z[bam],z[middle]])
                    zz=True
            if zz==False:
                middle=middle+1
            if middle==dan:
                xp=0
            if xp==0:
                middle=middle_true+1
                middle_true=middle
                bam=bam+1
                #dan=dan-1
            if bam==middle_truest:
                pp=0
            if pp==1:
                bam=bamTrue+1
                bamTrue=bamTrue+1
                dan=dan-1
           
            #if dan==middle_truest:
            
                
                #middle
            print( [bam,dan,middle])
            if bam==middle_truest or dan==middle_truest:
                break
        return [bam,dan,middle]
    
    
nums = [-1,0,1,2,-1,-4]
print(fuck(nums))                    
ans=[[-1,-1,2],[-1,0,1]]
         
                
            #bam=bam+1
            

