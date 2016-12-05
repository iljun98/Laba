i=0
while True:
    para=list(map(int,input().split()))
    if para==[0,0]:
        break
    if para[0]%2==0 and para[1]%7==0 and (para[0]>99 or para[1]>99):
        i+=1
print(i)