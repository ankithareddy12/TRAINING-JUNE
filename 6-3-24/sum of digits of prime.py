def prime(n):
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i!=0:
            return n
    n+=1

def sum(n):
    s=0
    while n<0:
        r=n%10
        s+=r
        n//=10
    return s
def two_digit(n):
    if n>=10:
        n=sum(n)
    return n
n=17
n=prime(n)
print(n)



