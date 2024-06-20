"""n = int(input())
while n:
    a = input()
    c = input()
    result = all(char in c for char in a)
    print(result)
    n -= 1
"""


def str(a, c):
    a_letters = [char.lower() for char in a if char.isalpha()]
    c_letters = [char.lower() for char in c if char.isalpha()]
    return all(char in c_letters for char in a_letters)

a ="abcdefghijklmnopqrstuvwxyz"
#c ="the 4quick br$%^own foENDx j45umps o.ver the lazy dog"
c="qwweer yuiop asdfvgh JKL mnbvlkjcxz"
result = str(a, c)
print(result)



a ="abcdefghijklmnopqrstuvwxyz"
#c ="the 4quick br$%^own foENDx j45umps o.ver the lazy dog"
c="qwweer yuiop asdfvgh JKL mnbvlkjcxz"
for i in a:
    if i in c:
        print("yes")
        break
    else:
        print("no")
        
        
c ="the 4quick br$%^own foENDx j45umps o.ver the lzy dog"       
d={}
for i in c:
    if i.islower():
        if i not in d:
            d[i]=i
print(d)
if len(d)==26:
    print("yes")
else:
    print("no")
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        