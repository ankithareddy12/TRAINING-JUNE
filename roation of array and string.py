#rotations of array and string
arr=[1,2,3,4,5]

d=2
arr=arr[d:]+arr[:d]#left
print(arr)


arr="ankitha"

d=2
arr=arr[-d:]+arr[:-d]#right
print(arr)


s="123"
n=2
temp=s+s
l1=len(s)
print(temp[n:l1+n])