"""s="the sky is blue"
i=s.split()
print(i)
r=i[::-1]
print(r)


nums=[3,2,2,3]
val=3
r=[]
x=sorted(nums)
print(x)
for x in nums:
    if x!=val:
        r.append(x)

print(r)


n=[1,1,2]
i=0
j=1
n1=len(n)
while j<n1:
    if n[j]==n[i]:
        j+=1
    else:
        n[i+1]==n[j]
        i+=1
        j+=1
print(i+1)
        
def subset(s):
    r=[]
    for i in range(len(s)):
        for j in range(i+1,len(s)+1):
            r.append(s[i:j])
    return r
def is_palindrome(s):
    return s==s[::-1]
    
s="babad"
x=subset(s)


for i in x:
    if is_palindrome(i):
        print("Palindrome:", i)
class Solution(object):
    def longestPalindrome(self, s):
        

        n = len(s)
        longest = ""
        for i in range(n):
            for j in range(i + 1, n + 1):
                substring = s[i:j]
                if self.is_palindrome(substring) and len(substring) > len(longest):
                    longest = substring
        return longest
    
    def is_palindrome(self, s):
        return s == s[::-1]"""

s = "anagram", t = "nagaram"
print(True is sorted(s)==sorted(t))

        c=int(a,2)+int(b,2)
        return bin(c)[2:]
        