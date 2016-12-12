a=[1,2,3,4,5,6]
b=[13,13,-1,33,12321,12321]
c=list(zip(a,b))
print(c)
c.sort(key=lambda x:(-x[1],x[0]))
print(c)