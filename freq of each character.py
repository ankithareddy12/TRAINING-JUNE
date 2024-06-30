s="aabccccddd"
c=1
d={}
string=[]
for char in s:
    if char in d:
        d[char]+=1
    else:
        d[char]=1
for char,c in d.items():
    string.append(f"{char}{c}")
print(''.join(string))
    