def coins(coins, tar):
    n = len(coins)
    max_val = tar + 1  
    dp = [[max_val] * (tar + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        dp[i][0] = 1  

    for i in range(1, n + 1):
        for j in range(1, tar + 1):
            if coins[i - 1] <= j:
                dp[i][j] = min(dp[i - 1][j], 1 + dp[i][j - coins[i - 1]])
            else:
                dp[i][j] = dp[i - 1][j]

  
    if dp[n][tar] == max_val:
        return "Not possible"
    else:
        return dp[n][tar]

coins_list = [2, 3, 5, 6]
target_sum = 11
print(coins(coins_list, target_sum))
"""
def coins(coin,tar):
    n=len(arr)
    dp=[[0]*(tar+1) for _ in range(n+1)]
    
    for i in range(n+1):
        dp[i][0]==1
    for j in range(1, tar + 1):
        dp[0][j] = 1 

    for i in range(1, n + 1):
        for j in range(1, tar + 1):
            if coins[i - 1] == j:
                dp[i][j] = 1
            elif coins[i - 1] < j:
                dp[i][j] = dp[i - 1][j]
            elif coins[i - 1] > j:
                if dp[i - 1][j] != -1:
                    dp[i][j] = min(dp[i - 1][j], 1 + dp[i][j - coins[i - 1]])
                else:
                    dp[i][j] = 1 + dp[i][j - coins[i - 1]]
                    
    if dp[n][tar] == '0':
        return "Not possible"
    else:
        return dp[n][tar]

arr = [2, 3, 5, 6]
target_sum = 11
print(coins(arr, target_sum))"""