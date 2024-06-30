'''The function accepts an integers sum and an integer array arr of size n. Implement the function to find the pair, (arr[j], arr[k]) where j!=k, Such that arr[j] and arr[k] are the least two elements of array (arr[j] + arr[k] <= sum) and return the product of element of this pai'''
arr=[5,2,4,3,9,7,1]
n=len(arr)
sum=9
if n<2:
    print("-1")
    
arr=sorted(arr)
for i in range(n-1):
    if arr[i]+arr[i+1]<sum:
        print(arr[i]*arr[i+1])
        break
    else:
        print('0')