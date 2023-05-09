def move_zeros(lst):
    
    i=0
    while i<len(lst):
        if lst[i]==0:
            lst.remove(0)
            lst.append(0)
            
            #i=i-2
        i=i+1
    return lst

lst=[9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]
print(move_zeros(lst))