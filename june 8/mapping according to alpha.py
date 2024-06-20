"""alpha="polikujmnhytgbvfredcxswqaz"
x='abbcdd'
z=[]
for i in x:
    if i in alpha:
        y=alpha.index(i)
        z.append(y)
print(z)
b=sorted(z)

s=""
for i in b:
    s    +=alpha[i]
print(s)"""
 
 
n=int(input())
while(n):
    a=input()
    c=input()
    s=' '
    for i in a:
        if i in c:
            s=s+(i*c.count(i))
    print(s)
    n=n-1
        