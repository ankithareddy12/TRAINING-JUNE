def is_prime(n):
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True


def dig(n):
    s=0
    while n>0:
        r=n%10
        s+=r
        n//=10
    return s
def two_dig(n):
    while n>=10:
        n=dig(n)
    return n
def chk_prime(n):
    while True:
        num=two_dig(n)
        if is_prime(num):
            return n
        n+=1
n=538
x=chk_prime(n)
print(x)

