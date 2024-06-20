#sort
"""l1=[2,5,7,9]
l2=[1,3,6,7,10,13]
l3=l1+l2
l3.sort()
print(l3)

l1=list(map(int,input().split(' ')))
l2=list(map(int,input().split(' ')))
def sort_function(l1,l2):
    i=0
    j=0
    c=[]
    while i<len(l1) and j<len(l2):
        if l1[i]<l2[j]:
            c.append(l1[i])
            i+=1
        else:
            c.append(l2[j])
            j+=1
    while i<len(l1):
        c.append(l1[i])
        i+=1
    while j<len(l2):
        c.append(l2[j])
        j+=1
    return c
print(sort_function(l1,l2))

# input aaaabb op=a4b2
x="aaabbaaaaddd"
def string(s):
    x=[]
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            count += 1
        else:
            x.append(s[i-1]+str(count))
            count=1
        
    x.append(s[-1]+str(count))
    return ''.join(x)

input_str= "aaabbaaaaddd"
output_str= string(input_str)
print(" ", output_str)

def string(s):
    x= []
    i = 0
    while i < len(s):
        count = 1
        while i + 1 < len(s) and s[i] == s[i + 1]:
            i += 1
            count += 1
        x.append(s[i] + str(count))
        i += 1
    return ''.join(x)

input_str = "aaabbaaaaddd"
output_str = string(input_str)
print(" ", output_str)

3 - 4
5 - 1
4 - 2
6 - 2
7 - 2
1 - 1
2 - 1
8 - 2
x=[3,5,4,3,6,7,1,2,4,3,3,7,6,8,8]
d={}
for i in x:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
for i, j in d.items():
    print(i,"-" ,j)
        
a=[3,5,4,3,6,7,1,2,4,3,3,7,6,8,8]    
b=[]
for i in a:
    if(i not in b):
        b.append(i)
for i in b:
    print(i,"-",a.count(i))

#find lower upper and special charac
lv=0  
uv=0  
lc=0  
uc=0 
d=0  
sp=0 
s="f46feLK9y56u#@&56hIjbn6KJhA"
vow="aeiouAEIOU"
for i in s:
    if i.islower() and i in vow:
        lv+=1
    elif i.isupper() and i in vow:
        uv+=1
    elif i.isdigit():
        d+=1
    elif i.islower() and i not in vow:
        lc+=1
    elif i.isupper() and i not in vow:
        uc+=1
    elif(not i.isalnum()):
        sp+=1
print("lv-",lv)
print("uv-",uv)
print("lc-",lc)
print("uv-",uc)
print("d-",d)
print("sp-",sp)

#lower to upper
def convert(s):
    vowels = 'aeiou'
    result = ''
    for char in s:
        if char.lower() in vowels and char.islower():
            char = char.upper()
        result += char
    return result

str="placements"
x= convert(str)
print(x)
        
#divisible by 7
a=300
b=400
c=(400/7)-(300/7)
print(int(c))

a=300
b=400
c=0
for i in range(300,400+1):
    if i%7==0:
        c+=1
print(c)

#prime and if not next prime
def prime(n):
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

def next_prime(n):
    next=n+1
    while True:
        if prime(next):
            return next
        next+=1
n=14 
if prime(n):
    print("true")
else:
    next_num=next_prime(n)
    print(next_num)

#count of prime
def prime(n):
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

c=0
s=6788
s=str(s)
for i in s:
    i=int(i)
    if prime(i):
        c+=1
print(c)


n=5678
c=0
while(n):
    if(n%10 in [2,3,5,7]):
        c+=1
    n=n//10
print(c)"""

#password validation
def password(pwd):
    d=any(char.isdigit() for char in pwd)
    up=any(char.isupper() for char in pwd)
    lw=any(char.islower() for char in pwd)
    sp=any(not char.isalnum() for char in pwd)
    c=0
    if not d:
        c+=1
    if not up:
        c+=1
    if not lw:
        c+=1
    if not sp:
        c+=1
    addi=8-len(pwd) if len(pwd)<8 else 0
    tot=max(c,addi)
    if tot == 0:
        print("noting to add")
    else:
        print(f"{tot}")
x="abcdef227"
password(x)

n='12345aa*'
if len(n)<8:
    print("Invalid")
l=0
u=0
d=0
s=0
for i in n:
    if i.islower():
        l=1
    elif i.isupper():
        u=1
        
    elif i.isdigit():
        d=1
        
    elif not i.isalnum():
        s=1
m=4-(l+u+d+s)
if (len(n)+m)<8:
    print(8-len(n))
else:
    print(m)

        









    



        
    
    
    
    
    