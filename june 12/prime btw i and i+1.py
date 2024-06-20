#x=[4,8,14,22,36,68]
#all are non primes then find primes btw every i and i+1
"""
def is_prime(n):
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n % i==0:
            return False
    return True


def max_prime(a,b):
    max_prime=None
    for x in range(a+1,b):
        if is_prime(x):
            if max_prime is None or x > max_prime:
                max_prime=x
    return max_prime

arr=[14,16,20,22]

max_primes=[]

for i in range(len(arr)-1):
    a, b = arr[i],arr[i+1]
    maxi= max_prime(a,b)
    max_primes.append(maxi)

print(max_primes)
print(sum(max_primes))

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

x=[4,8,14,22,36,68]

l=[]

for i in range(1,len(x)):
    start=x[i-1]
    end= x[i]
    for j in range(end -1, start - 1, -1):
        if is_prime(j):
            max_prime = j
            break
    if max_prime is not None:
        l.append(max_prime)

sum_of_max_primes = sum(l)
print(sum_of_max_primes)"""

def isprime(x):
    for i in range(2,(x//2)+1):
        if(x%i==0):
            return 0
    return 1
def lprime(n,m):
    for i in range(m-1,n-1):
        if(isprime(i)):
            return i
    return 0

a=[4,8,14,22,36,68]
s=0
for i in range(len(a)-1):
    s=s+lprime(a[i],a[i+1])
print(s)























