'''The function accepts an integers arr of size ’length’ as its arguments you are required to return the sum of second largest  element from the even positions and second smallest from the odd position of given ‘arr’'''
arr=[3,2,1,7,5,4]
n=len(arr)
e=[]
o=[]
for i in range(0,n):
    if i%2==0:
        e.append(arr[i])
    else:
        o.append(arr[i])
e=sorted(e)
print(e)
o=sorted(o)

print(o)
print(e[-2]+o[1])
                 
    