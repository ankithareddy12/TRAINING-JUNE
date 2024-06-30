"""Problem Description :
The function accepts two positive integers ‘r’ and ‘unit’ and a positive integer array ‘arr’
of size ‘n’ as its argument ‘r’ represents the number of rats present in an area, ‘unit’ is the amount
of food each rat consumes and each ith element of array ‘arr’ represents the amount of food present in ‘i+1’
house number, where 0 <= i

arr=[2,8,3,5,7,4,1,2]
n=len(arr)
r=7
unit=2
total=r*unit
print(total)
sum=0
c=0
for i in arr:
    sum=sum+i
    c+=1
    if sum>=total:
        break
print(c)"""


