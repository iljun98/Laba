par=[]
while True:
    c=int(input())
    if c==0:
        break
    par+=[c]
print(par.count(max(par)))