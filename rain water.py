#arr=[2,7,2,3,6,7,1,0,5,7]
arr=[3,5,9,6,8,10]
n=len(arr)
l=[]
r=[]
x=0
c=0
c1=0
for i in range(1,n-1):
    l=max(arr[:i+1])
    print(l,end=" ")
    c+=1
    r=max(arr[i:])
    print(r)
    
    x+=max(0,min(l,r)-arr[i])

print(c)
print(c1)



"""
arr=[4,3,4,5,6,1,0,6,7]
for i in range(1,len(arr)-1):
    print(arr[:i])
    n=max(arr[:i])
    print(arr[i+1:])
    p=(max(arr[i+1:]))
    print(max(0,min(n,p)-arr[i]))"""
    