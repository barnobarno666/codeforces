def fuck(nums):
 
        num=[str(i) for i in nums]
        num.sort(reverse=True)
        if len(nums)==2:
            z=num[0]
            f=num[1]
            a=False
            for i in range(len(num[0])):      
                             
                    if num[0][-(i+1)] < num[+1][-1]:
                            a=True
                            break
            if a==True:
                num[0],num[1]=num[+1],num[0]               
            return ''.join(i for i in num)

                    
        if len(nums)!=2:    
            for i in range(len(nums)-1):
                a=False
                if num[i][-1]=='0'  and len(num[i+1]) < len(num[i]) and num[i+1][0]==num[i][0]:
                    num[i],num[i+1]=num[i+1],num[i]
                    #print('suck')
                elif num[i][-1]<=num[i+1][-1] and len(num[i+1]) < len(num[i]) and z[:len(f)]==f :
                    print('FUCK')
                    for i in range(len(num[i]) -len(num[i+1]) ):
                        if num[i][-(i+1)] < num[i+1][-1]:
                            a=True
                            break
                    if a==True:
                        num[i],num[i+1]=num[i+1],num[i]
                    
        return ''.join(i for i in num)
    












[3,30,34,5,9]
"""Output
"9534303"
Expected
"9534330"

Output
"343233432"
Expected
"343234323"

"""



#nums = [3,30,34,5,9]
#nums =[111311, 1113]
#nums=[34323,34329,39]


#Input
nums =[1,2,30]
print(fuck(nums))