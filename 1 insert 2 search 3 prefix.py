n=int(input())
l=[]

def prefix(l, n,c=0):
    for i in l:
        if i.startswith(n):
            c+=1
            return c
    return False


for i in range(n):
    m,n=input().split(' ')
    if m=='1':
        l.append(n)
    elif m=='2':
        if n in l:
            print("True")
        else:
            print("False")
    elif m=='3':
        print(prefix(l,n,0))
    elif m=='4':
        l.remove(n)
        print(l)
        

        
        
"""ip:7
1 school
1 world
1 word
1 scholar
2 word
2 wood
3 sch
#
op:
True
False
true
1 - insert
2- word there or not
3. prefix in word

d = {
    '1':['school','world','word','scholar'],
    '2':['word','wood'],
    '3':['sch']
}
print(d['1'])
for i in d['2']:
    if i in d['1']:
        print("True")
    else:
        print("False")

for i in d['3']:
    if i in d['1']:
        print("True")
    else:
        print("False")
prefix="sch"
prefix_p=False

for item in d['1']:
    if item.startswith(prefix):
        is_prefix_present=True
        break
if is_prefix_present:
    print("yes")
else:
    print("no")"""
          


    


    
