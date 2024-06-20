"""
class Solution:
    def is_palindrome(self, n):
        return str(n) == str(n)[::-1]

    def digit_sum(self, n):
        sm = 0
        for i in str(n):
            sm += int(i)
        return sm
    
    def check(self, n):
        sum_of_digits = self.digit_sum(n)
        if self.is_palindrome(sum_of_digits):
            return 1
        return 0

# Example usage
sol = Solution()
n = 56
x = sol.check(n)
print(x)  # Output: 1




def substring(n,k,str=''):
    if k==0:
        print(str)
    else:
        for i in n:
            substring(n,k-1,str+i)
n=['a','b','c']
k=3
substring(n,k)"""



















