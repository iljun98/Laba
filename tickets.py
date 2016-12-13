n=int(input())
a=[]
for i in range(n):
    a.append(tuple(map(int,input().split())))
def price(n,a):
    if n==1:
        return a[0][0]
    if n==2:
        return min((a[0][0]+a[1][0]),a[0][1])
    cost=[a[0][0],min((a[0][0]+a[1][0]),a[0][1]),min((a[0][0]+a[1][0]+a[2][0]),(a[0][2]),(a[0][0]+a[1][1]),(a[0][1]+a[2][0]))]+[None]*(n-2)
    if n>3:
        for i in range(3,n):
            cost[i]=min((cost[i-3]+a[i-2][2]),(cost[i-2]+a[i-1][1]),(cost[i-1]+a[i][0]))
    return cost[n-1]
print(price(n,a))