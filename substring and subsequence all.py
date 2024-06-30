#substring
s="abcd"
n=len(s)
for i in range(n):
    for j in range(i+1,n+1):
        print(s[i:j])
        
#subsequence
def find_sub(s):
    sub=[]
    def solve_sub(i,index):
        if index==len(s):
            sub.append(i)
        else:
            solve_sub(i+s[index],index+1)
            solve_sub(i,index+1)
    solve_sub('',0)
    return sub
s="ggg"
x=find_sub(s)
print(x)

        
# distinct subsequence
def find_sub(s):
    sub=set()
    def solve_sub(i,index):
        if index==len(s):
            sub.add(i)
        else:
            solve_sub(i+s[index],index+1)
            solve_sub(i,index+1)
    solve_sub('',0)
    return sub
s="ggg"
x=find_sub(s)
print(x)
print(len(x))

#distinct occurance
def distinct_occurrence(s, t):
    m=len(s)
    n=len(t)
    dp=[[0]*(n+1) for _ in range(m+1)]
    for i in range(m+1):
        dp[i][0]=1
    for i in range(m+1):
        for j in range(n+1):
            if s[i-1]==t[j-1]:
                dp[i][j]=dp[i-1][j-1]+dp[i-1][j]
            else:
                dp[i][j]=dp[i-1][j]
    return dp[m][n]
    
s = "banana"
t = "ban"
result = distinct_occurrence(s, t)
print(result)  # Output: 3


#largest subsequence
def large(s1, s2):
    def lcm(i, j):
        if i == 0 or j == 0:
            return 0
        elif s1[i - 1] == s2[j - 1]:
            return 1 + lcm(i - 1, j - 1)
        else:
            return max(lcm(i - 1, j), lcm(i, j - 1))

    return lcm(len(s1), len(s2))

s1 = "ABCBDAB"
s2 = "BDCAB"
x = large(s1, s2)
print(x)  # Output: 4











            