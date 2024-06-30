n='23GF'
print(int(n,17))

s='23GF'
n="0123456789ABCDEFG"
d=0
p=0
for i in reversed(s):
    d1=n.index(i)
    d+=d1*(17**p)
    p+=1
print(d)