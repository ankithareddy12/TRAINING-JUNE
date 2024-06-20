def coprime(a, b):
    while b != 0:
        a, b = b, a % b
    
    if a == 1:
        return True
    else:
        return False

a = 15
b = 28
if  coprime(a, b):
    print("True")
else:
    print("False")


def are_coprime(a, b):
    x = min(a, b)
    for i in range(2, x + 1):
        if a % i == 0 and b % i == 0:
            return False
    return True


a = 15
b = 28
if are_coprime(a, b):
    print("True")
else:
    print("false")


