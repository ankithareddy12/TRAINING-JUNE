"""
def lcs(text1, text2, m, n):
    if m == 0 or n == 0:
        return 0
    elif text1[m-1] == text2[n-1]:
        return 1 + lcs(text1, text2, m-1, n-1)
    else:
        return max(lcs(text1, text2, m, n-1), lcs(text1, text2, m-1, n))

def longestCommonSubsequence(text1, text2):
    m = len(text1)
    n = len(text2)
    return lcs(text1, text2, m, n)

text1 = "abcd"
text2 = "axbdc"
c = longestCommonSubsequence(text1, text2)
print(c)  # Output: 3"""

#longest subsequence
s1="abcd"
s2= "axbdc"
m=[]

for i in range(len(s1)+1):
    l=[0]*(len(s2)+1)
    m.append(l)
for i in range(1,len(s1)+1):
    for j in range(1,len(s2)+1):
        if s1[i-1]==s2[j-1]:
            m[i][j]=m[i-1][j-1]+1
        else:
            m[i][j]=max(m[i][j-1],m[i-1][j])
print(m[len(s1)][len(s2)])

    
    #substring longest
s1="abcd"
s2= "axbdc"
u=len(s1)
v=len(s2)
s=''
m=[]
length=0
substring=' '
for i in range(len(s1)+1):
    l=[0]*(len(s2)+1)
    m.append(l)
for i in range(1,len(s1)+1):
    for j in range(1,len(s2)+1):
        if s1[i-1]==s2[j-1]:
            m[i][j]=m[i-1][j-1]+1
            while u>0 and v>0:
                if (s1[u-1]==s2[v-1]):
                    s=s+s1[u-1]
                    u=u-1
                    v=v-1
                else:
                    if(m[u-1][v]>m[u][v-1]):
                        u=u-1
                    
                    else:
                        v=v-1
                

print(s)

#substring longest
s1="abcd"
s2="axbdc"
u=len(s1)
v=len(s2)
m=[]
s=""
for i in range(u+1):
    l=[0]*(v+1)
    m.append(l)
for i in range(1,u+1):
        for j in range(1,v+1):
            if(s1[i-1]==s2[j-1]):
                m[i][j]=m[i-1][j-1]+1
            else:
                m[i][j]=max(m[i][j-1],m[i-1][j])
print(m[u][v])
while u>0 and v>0:
    if(s1[u-1]==s2[v-1]):
        s=s+s1[u-1]
        u=u-1
        v=v-1
    else:
        if(m[u-1][v]>m[u][v-1]):
            u=u-1
        else:
            v=v-1
s=s[::-1]
print(s)

