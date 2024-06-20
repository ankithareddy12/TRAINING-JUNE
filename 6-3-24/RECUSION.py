"""

def fun(n):
    if n==3:
        return
    print(n)
    fun(n+1)
    print(n)
    
    
fun(1)

#sum of numbers
def fun(x,s):
    if x==len(a):
        return s
    s+=a[x]
    return fun(x+1,s)
    
    
a=[1,2,3,4]
print(fun(0,0))

#sum of 2 lists even
def fun(x,y,s1,s2):
    if x==len(a) and y==len(b):
        return s1,s2
    if a[x]%2==0:
        s1=s1+a[x]
    if b[y]%2!=0:
        s2=s2+b[y]   
    return fun(x,y,s1,s2)
    
    
a=[1,2,3,4]
b=[1,2,3,4]
print(fun(0,0,0,0))

#sum of numbers

def sum(n):
    if n == 0:
        return 0
    else:
        return n + sum(n - 1)
n = 10
result = sum(n)
print(result)



#sum of even numbers

def sum(n):
    if n<=0:
        return 0
    elif n%2==0:
        return n+sum(n-2)
    else:
        return sum(n-1)
n=12
r=sum(n)
print(r)

#sum of even numbers
def fa(x):
    if(x==0):
        return 0
    return x+fa(x-2)
n=13
if n%2==0:
    print(fa(n)):
else:
    print(fa(n-1))"""

a=[5,8,9,2,4,7]
n=len(a)
if n%2==0:
    print("yes")
else:
    print("no")


a=[5,8,9,2,4,2,4]
x=(a[0]+a[-1])/2
if x%2==0:
    print("yes")
else:
    print("no")


