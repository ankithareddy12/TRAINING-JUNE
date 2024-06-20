def longest_common_subsequence_length(str1, str2):
    m, n = len(str1), len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]

str1 = "aba"
str2 = "a"

result = longest_common_subsequence_length(str1, str2)
print( result)
"""def find_all_common_subsequences(str1, str2):
    if len(str1) == 0 or len(str2) == 0:
        return ['']

    if str1[-1] == str2[-1]:
        common_subs_without_last = find_all_common_subsequences(str1[:-1], str2[:-1])
        return [sub + str1[-1] for sub in common_subs_without_last] + common_subs_without_last
    else:
        subs1 = find_all_common_subsequences(str1[:-1], str2)
        subs2 = find_all_common_subsequences(str1, str2[:-1])
        return subs1 + subs2

# Example usage:
string1 = "abcd"
string2 = "axbdc"
common_subsequences = find_all_common_subsequences(string1, string2)
print(common_subsequences)"""
