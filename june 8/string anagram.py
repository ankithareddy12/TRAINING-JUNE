def leftrotate(s, d):
    tmp = s[d : ] + s[0 : d]
    return tmp

def rightrotate(s, d):
  
   return leftrotate(s, len(s) - d)
s='school'
x=rightrotate(s,3)
y=leftrotate(x,2)
z=leftrotate(y,1)
print(y[0])
print(x[0])
print(z[0])
ans=y[0]+x[0]+z[0]
print(ans)
def printsub(s):
    sub=[]
    for i in range(len(s) - 2):
        sub.append(s[i:i+3])
    return sub
s='school'
sub=printsub(s)
print(sub)
found = False
for substring in sub:
    if sorted(substring) == sorted(ans):
        found = True
        print("yes")
        break

if not found:
    print("no")
    