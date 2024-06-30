'''int findCount(int arr[], int length, int num, int diff);

The function accepts an integer array ‘arr’, its length and two integer variables ‘num’ and ‘diff’. Implement this function to
find and return the number of elements of ‘arr’ having an absolute difference of less than or equal to ‘diff’ with ‘num’.
Note: In case there is no element in ‘arr’ whose absolute difference with ‘num’ is less than or equal to ‘diff’, return -1'''

def findCount(arr,num,diff):
    n=len(arr)
    c=0
    for i in range(n):
        if abs(arr[i]-num)<=diff:
        
            c+=1
    if c:
        return c
    else:
        return 0
    
arr=[12,3,14,56,77,13]
num=13
diff=2
x=findCount(arr,num,diff)
print(x)