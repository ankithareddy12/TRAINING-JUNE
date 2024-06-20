"""a=[13,9,4,10,5,7]
x=max(a)
print(x)
a.remove(x)
print(a)
for i in a:
    while i>=1:
        x=max(a)
        a.remove(x)
print(a)
"""

def fun(l):
    if len(l) == 0:
        return 0
    if len(l) == 1:
        return l[0]
    if len(l) == 2:
        return max(l)
    
    le = l[0] + fun(l[2:])
    ri = l[1] + fun(l[3:])
    return max(le, ri)

# Example usage:
houses = [13, 9, 4, 10, 5, 7]
print("Maximum amount of gold stolen:", fun(houses))






















    

    
    
 
    
