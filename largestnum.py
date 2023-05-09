def fuck(nums):
 
        num=[ str(i) for i in nums]
        num.sort(reverse=True)
        return num
        f=''
        if len(num)==2:
            z=str(nums[0])
            f=str(nums[1])
            if int(f+z)>int(z+f):
                return (f+z)

            return z+f
       
            
        for i in range(len(num)-1):
            z=num[i]
            f=num[i+1]
            print(z[0],f[0])
            if num[i][0]==num[i+1][0]:
                return f
                if f+z>=z+f :num[i],num[i+1]=num[i+1],num[i]



        return ''.join(i for i in num)
nums =[1,2,30]
nums = [3,30,34,5,9]
print(fuck(nums))