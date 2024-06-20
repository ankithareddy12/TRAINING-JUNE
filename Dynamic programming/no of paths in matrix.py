def path(m,n):
    if n==1 or m==1:
        return 1
    elif n==0 or m==0:
        return 0
    else:
        return path(m-1,n)+path(m,n-1)

print(path(4,3))

#top left
m=4
n=4
dp=[[0]*n for _ in range(m)]

for i in range(m):
    dp[i][0]=1
for j in range(n):
    dp[0][j]=1
    
for i in range(1,m):
    for j in range(1,n):
        dp[i][j]=dp[i-1][j]+dp[i][j-1]
print(dp)
    
print(dp[m-1][n-1])

#all
def number_of_unique_paths(m, n):
    dp = [[0] * n for _ in range(m)]
    
    dp[0][0] = 1  

    for i in range(m):
        for j in range(n):
            if i>0:
                dp[i][j]+=dp[i-1][j]
            if j>0:
                dp[i][j]+=dp[i][j-1]
            if i<m-1:
                dp[i][j]+=dp[i+1][j]
            if j<n-1:
                dp[i][j]+=dp[i][j+1]

    return dp[m-1][n-1]

m=4
n=3
print(number_of_unique_paths(m, n))
     



