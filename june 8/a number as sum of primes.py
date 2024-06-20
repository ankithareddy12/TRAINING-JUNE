def is_prime(number):
    if number <=1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def sum(n):
    for i in range(1, n):
        if is_prime(i) and is_prime(n - i):
            print(i,n-i)
            return True
    return False

n=12
if sum(n):
    print("True")
else:
    print("false")