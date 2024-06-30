'''To solve the problem of finding the Nth term in the given series where odd terms are from the Fibonacci sequence and even terms are prime numbers in ascending order, we can break down the solution into two main parts:

Generating Fibonacci Sequence:

Fibonacci sequence starts with 1, 2, and each subsequent number is the sum of the two preceding ones (1, 2, 3, 5, 8, ...).
Generating Prime Numbers:

Prime numbers are numbers greater than 1 that have no divisors other than 1 and themselves (2, 3, 5, 7, 11, ...).
Finding the Nth Term:

Depending on whether N is odd or even, retrieve the corresponding term from either the Fibonacci sequence or the list of prime numbers'''

def is_prime(num):
    """ Function to check if a number is prime """
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def generate_fibonacci(n):
    """ Function to generate first n Fibonacci numbers """
    fib = [1, 2]
    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])
    return fib

def generate_primes(n):
    """ Function to generate first n prime numbers """
    primes = []
    num = 2
    while len(primes) < n:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes

def find_nth_term(n):
    fib_sequence = generate_fibonacci(n)
    prime_sequence = generate_primes(n)
    
    if n % 2 == 1:
        return fib_sequence[(n // 2)]
    else:
        return prime_sequence[(n // 2) - 1]

# Reading input and computing result
n = int(input().strip())
result = find_nth_term(n)
print(result)
