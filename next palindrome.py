"""def is_palindrome(num):
    num_str=str(num)
    return num_str==num_str[::-1]

def palindrome(num):
    while True:
        num+=1
        if is_palindrome(num):
            print("True")
            break
    print(num)

num=56472
palindrome(num)
"""
n=1234
n=str(n)
x=n[::-1]
y=n
print(y)
z=y[:2]
print(z)
z1=z[::-1]
print(z1)
z2=''.join(z+z1)
print(z2)
if z2<y:
    z=z+1
    z1=z[::-1]
    z2=''.join(z+z1)
    print(z2)
    

    



