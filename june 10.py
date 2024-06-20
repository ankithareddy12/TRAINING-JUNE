def rec(l):
    l1 = []
    l2 = []
    x = set()
    
    for i in l:
        if i not in x:
            l1.append(i)
            x.add(i)
        else:
            l2.append(i)
    
    return l1, l2

def check(l):
    result = []
    
    while l:
        l1, l2 = rec(l)
        result.append(l1)
        l = l2  
    
    return result

l = [1, 2, 3, 4, 1, 2, 3, 1, 2]
output = check(l)

for sublist in output:
    print(sublist)
