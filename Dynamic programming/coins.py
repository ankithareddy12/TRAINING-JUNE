def minCoins(coins,amount):
    inf=10**9  
    dp = [inf]*(amount + 1)
    dp[0]=0
    
    for i in range(1,amount+1):
        for coin in coins:
            if i>=coin:
                dp[i]=min(dp[i],dp[i - coin] + 1)
    
    return dp[amount]

coins = [1,3,4,5]
amount = 17
result = minCoins(coins, amount)
print(result)


a=[3,4]
n =5
l=[float('inf')]* (n+1)
l[0]=0

for i in range(1,n+1):
    for coin in a:
        if i>=coin:
            l[i]=min(l[i],l[i-coin]+1)

print(l[n])

def fun():
    l1=[-1]*(n+1)
    l1[0]=0
    for i in l:
        for j in range(1,n+1):
            if j>=i:
                if l1[j-i]!=-1:
                    if l1[j]!=-1:
                        l1[j]=min(l1[j],l1[j-i]+1)
                    else:
                        l1[j]=l1[j-i]+1
    print(l1[-1])
l=[1,3,4,5]
n=17
fun()