'''Question: Write a program in C such that it takes a lower limit and upper limit as inputs
and print all the intermediate palindrome numbers.'''
def is_palindrome(n):
    n=str(n)
    #n_str=n[::-1]
    #if n==n_str:
        #return True
    #else:
        #return False
    return n==n[::-1]

n=101
print(is_palindrome(n))

def is_palindrome(n):
    n=str(n)
    return n==n[::-1]
def btw_palindrome(n1,n2):
    for n in range(n1,n2+1):
        if is_palindrome(n):
            print(n,end=",")

n1=100
n2=200
print(btw_palindrome(n1,n2))

