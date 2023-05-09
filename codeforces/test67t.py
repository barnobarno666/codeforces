def cunt(a,b):
    return sum(x.count(b) for x in a)
a=[[1,4],[3,7],[7,9]]
print(cunt(a, 7))