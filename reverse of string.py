#all 0(n)
a='abc'
s=a[::-1]
print(s)

a="abcd"
print(''.join(reversed(a)))

a="asdf"
r=""
for i in a[::-1]:
    r+=i
print(r)

