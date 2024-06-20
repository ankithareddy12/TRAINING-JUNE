str1="tu5g2k1h8"
str2="g5g8gd6h3"

d1=[]
d2=[]
for i in str1:
    if i.isdigit():
        d1.append(i)
print(d1)
for i in str2:
    if i.isdigit():
        d2.append(i)
print(d2)
digits=list(set(d1+d2))
print(digits)
n=len(digits)
digits.sort(reverse=True)
print(digits)
if (int(digits[-1])%2==0):
    print(''.join(digits))
else:
    for i in range(len(digits)-2,-1,-1):
        if (int(digits[i])%2==0):
            digits.append(digits.pop(i))
            print(''.join(digits))
            break
        else:
            print(-1)

print(digits)
