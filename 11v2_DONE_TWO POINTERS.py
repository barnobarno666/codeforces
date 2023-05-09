#
def fuck(height):
    bam=0
    dan=len(height)-1
    #maxx=0
    maxx=min(height[bam],height[dan])*abs(dan-bam)
    while True:
        #print(bam,dan,maxx)
        if height[bam]>=height[dan]:
            dan=dan-1
        elif height[bam]<height[dan]:
            bam=bam+1
        jaja=min(height[bam],height[dan])*abs(dan-bam)
        if jaja>maxx:
            maxx=jaja
        if bam-dan==1:
            break
    return maxx   

#height=[1,2,3,4,5,6,7,8,9,10]
height=[1,1,9]
print(fuck(height))        

        
        
    
    