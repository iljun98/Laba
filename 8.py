n=int(input())
Prices=list(map(int,input().split()))
def price(n,Prices):
    cost=[Prices[0],Prices[1]]+[None]*(n-2)
    if n>2:
        for i in range(2,n):
            cost[i]=Prices[i]+min(cost[i-1],cost[i-2])
    return cost[n-1]
print(price(n, Prices))