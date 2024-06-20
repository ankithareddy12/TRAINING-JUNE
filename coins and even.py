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



def longest_even_number(str1, str2):
    digits1 = [char for char in str1 if char.isdigit()]
    digits2 = [char for char in str2 if char.isdigit()]

    unique_digits = list(set(digits1 + digits2))

    unique_digits.sort(reverse=True)

    dp = [["" for _ in range(2)] for _ in range(len(unique_digits) + 1)]

    for i in range(1, len(unique_digits) + 1):
        digit = unique_digits[i - 1]
        for j in range(2):
            dp[i][j] = dp[i - 1][j]  
            if j == 1 and int(digit) % 2 == 0:  
                dp[i][j] = max(dp[i][j], dp[i - 1][0] + digit)
            elif j == 0:  
                dp[i][j] = max(dp[i][j], dp[i - 1][j] + digit)

    result = dp[len(unique_digits)][1]
    return result if result else "No even number can be formed"

str1="tu5g2k1h8"
str2="g5g8gd6h3"
print(longest_even_number(str1, str2))
