"""a=[3,4]
n=3
l=[float('inf')]*(n+1)
print(l)
l[0]=0

for i in range(1,n+1):
    for coin in a:

        if i>=coin:
            l[i]=min(l[i],l[i-coin]+1)

print(l[n])"""


a=[1,2,3,5]
n=4
l=[]
for i in range(0,n+1):
    l.append(i)    
for i in range(1,n+1):
    for coin in a:
        if i>=coin:
            l[i]=min(l[i],l[i-coin]+1)
        
print(l[n])




def min_coins(coins,tar):
    l=[[0]*(tar+1) for i in range(len(arr)+1)]
    for i in range(len(arr)+1):
        l[i][0]=0
    for j in range(1,tar+1):
        l[0][j]=-1
    for i in range(1,len(arr)+1):
        for j in range(1,tar+1):
            if arr[i-1]<=j:
                l[i][j]=min(l[i-1][j],1+l[i][j-arr[i-1]])
            else:
                l[i][j]=l[i-1][j]
    return l[len(arr)][tar]
arr=[3,4]
tar=5
print(min_coins(arr,tar))



