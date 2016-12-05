log=sorted(input().split())
d={}
for i in range(len(log)):
    tmp=log.count(log[i])
    d.update({log[i]:tmp})
    i+=tmp-1
finder=sorted(list(d.values())) #сортированный список количеств встречающихся товаров
max1=finder[-1]
maxi1=len(finder)-finder.index(max1)+1
max2=finder[finder.index(max1)-1]
maxi2=finder.index(max1)-finder.index(max2)
print(maxi1,maxi2)