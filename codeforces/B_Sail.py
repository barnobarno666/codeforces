# from sys import exit
# def pos_finder(a,h,o,c,s):
#     i=0
#     while i < (len(a)):
#         if h[0]!=0:
#             if  h[0]>0:
#                 for j in range(len(a)):
#                     if a[j]==' ':
#                         a[j]=='p'
#                         c[0]=c[0]+j
#                         break
#         i=i+1
# def neg_finder(a,h,o,c,s):
#     i=0
#     while i < (len(a)):
#         if h[0]!=0:
#             if  h[0]>0:
#                 for j in range(len(a)):
#                     if a[j]==' ':
#                         a[j]=='p'
#                         c[0]=c[0]+j
#                         break
#         i=i+1

from sys import exit
b=[int(x) for x in input().split()]
n=b[0]
b=b[1:]
#print(a)
a=list(input())
if b[-1]-b[1] >0 :
    if  b[-1]-b[1] > a.count('N'):
        print(-1) 
        exit()  
elif b[-1]-b[1] <0 : 
    if  abs(b[-1]-b[1]) > a.count('S'):
        print(-1)
        exit()
if b[0]-b[2] >0 :
    if   b[0]-b[2] > a.count('W'):
        print(-1 )
        exit()
elif b[0]-b[2] <0 : 
    if  abs(b[0]-b[2]) > a.count('E'):
        print(-1 )
        exit()  
c=[0,0]
h=[int(b[2]-b[0]),int(b[-1]-b[1])]
#print(h)
i=0
if i==0:

    if h[1]>0:
        while h[1]>0:
            for j in range(len(a)):
                if h[1]==0:break
                if a[j]=='N':
                    h[1]=h[1]-1
                    c[1]=j
                    #print(j)
    elif h[1]<0:
        while h[1]<0:
            for j in range(len(a)):
                if h[1]==0:break
                if a[j]=='S':
                    h[1]=h[1]+1
                    c[1]=j
    if h[0]>0:
        while h[0]>0:
            for j in range(len(a)):
                if a[j]=='E':
                    if h[0]==0:break
                    h[0]=h[0]-1
                    c[0]=j
                    #print(j)
                    
    elif h[0]<0:
        while h[0]<0:
            for j in range(len(a)):
                if h[0]==0:break
                if a[j]=='W':
                    h[0]=h[0]+1
                    c[0]=j 
                    #print(j)
  

print(max(c)+1)
