"""def combinations_recursive(lst, start=0, path=[], result=[]):
    if len(path) == 3:
        result.append(path)
        return result
    for i in range(start, len(lst)):
        combinations_recursive(lst, i + 1, path + [lst[i]], result)
    return result

l = [3, 2, 5, 4, 1, 6, 8]
r = combinations_recursive(l)
print(r)
def combine_recursive(lst, path=[], start=0):
    if len(path) == 3:
        return [path]
    if start >= len(lst):
        return []
    result = []
    for i in range(start, len(lst)):
        result += combine_recursive(lst, path + [lst[i]], i + 1)
    return result

def combinations(lst):
    return combine_recursive(lst)

l = [3, 2, 5, 4, 1, 6, 8]
r = combinations(l)
print(r)

def prime_factors(n):
    factors = []
    divisor = 2
    while divisor <= n:
        if n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        else:
            divisor += 1
    return factors

def number_as_sum_of_primes(n):
    prime_factors_list = prime_factors(n)
    if len(prime_factors_list) == 1:
        return [n] 
    else:
        primes_sum = []
        for factor in prime_factors_list:
            primes_sum.extend(prime_factors(factor)) 
        return primes_sum

# Example usage:
number = 12
sum_of_primes = number_as_sum_of_primes(number)
print(f"{number} as the sum of prime numbers: {sum_of_primes}")"""



alpha = "qwryupcsfoghjkldezxvbintma"
x = 'ativedoc'
mapped_chars = []

for i in x:
    if i in alpha:
        index = alpha.index(i)
        mapped_chars.append(alpha[index])

print(''.join(mapped_chars))























