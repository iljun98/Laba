li = [5,2,7,4,0,9,8,6]
c = 0
for n in range(0,len(li)):
    for i in range(len(li)-n):
        if li[i] > li[i+1]:
            li[i],li[i+1] = li[i+1],li[i]
            c += 1
print(c)