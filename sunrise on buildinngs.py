arr=[3,5,9,6,8,10]
n=len(arr)
l=[0]*n
r=[0]*n
s=0
m=0
m1=0
i = 0
while i<n:
    
    if arr[i]>m:
        m=arr[i]
    l[i]=m
    i += 1
i=n-1
while i>=0:
    if arr[i]>m1:
        m1=arr[i]
    r[i]=m1
    i-=1
print(len(set(l)))
print(len(set(r)))




"""
arr=[3,5,9,6,8,10]
l=[0]*len(arr)
r=[0]*len(arr)
m,m1=0,0
s=0
for i in range(len(arr)):
    if arr[i]>m:
        m=arr[i]
    l[i]=m
for i in range(len(arr)-1,-1,-1):
    if arr[i]>m1:
        m1=arr[i]
    r[i]=m1
print(set(l),set(r))"""