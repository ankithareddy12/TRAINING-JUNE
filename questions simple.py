print("hello world")
def number(n):
    if n%2==0:
        return "even"
    return 'odd'
def check(n):
    eo=number(n)
    return eo
n=3
print(check(n))
l=[4,3,3,4]
s=sum(l[0:4])
print(s)
print(max(l))
print(str(l[::-1]))
if str(l)==str(l[::-1]):
    print("yes")
else:
    print("no")
n=1412
r=0
while n!=0:
    d=n%10
    r=r*10+d
    n=n//10
print(r)
if n==r:
    print("yes")
else:
    print("no")
    
def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)
num=6
print(fact(num))

def isprime(n):
    if n<=1:
        return 1
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
        return True
def check(n):
    prime=isprime(n)
    return prime
n=6
print(check(n))
def fib(n):
    if n<=1:
        return n
    else:
        return fib(n-1)+fib(n-2)
num=5
print(fib(num))

c=30
f=c*(9/5)+32
print(f)

#substring
def get_substrings_of_length_k(s, k):
    substrings = []
    for i in range(len(s) - k + 1):
        substrings.append(s[i:i+k])
    return substrings

# Example usage
s = "Hello, World!"
k = 2
substrings = get_substrings_of_length_k(s, k)
print(substrings)

def subsequences(s):
    if len(s) == 0:
        return ['']  # Base case: an empty string has one subsequence, which is an empty string itself
    else:
        subseq = subsequences(s[1:])  # Recursive call to get subsequences of the rest of the string
        return subseq + [s[0] + sub for sub in subseq]

# Example usage
s = "abc"
result = subsequences(s)
print(result)
























