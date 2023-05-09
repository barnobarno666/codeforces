n=int(input()) #1,299,709
r=0
a=[1000000]
for i in range(1000000+1,100000000):
    if r>=n:break
    r=r+1
    print(i,end=' ')
    
# while True:
#     if len(a)>=n:break
#     for i in range(3,2299709):
#         if len(a)>=n:break
#         ll=0
#         for j in a:
#             if i%j==0:
#                 ll=1 
#         if ll==0:
#             a.append(i)
#         #print(a)
# for i in a:
#     print(i,end=' ')