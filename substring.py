def substring(s):
    x=[]
    n=len(s)
    for i in range(n):
        for j in range(i+1,n+1):
            x.append(s[i:j])
    return x
s="Abc"
sub=substring(s)
print(sub)