#Given an array of integers and a value, determine if there are any two integers in the array whose sum is equal to the given value.
def sum(arr,t):
    n=len(arr)
    for i in range(n):
        if arr[i]+arr[i+1]==t:
            return arr[i],arr[i+1]
            break
            
    
arr=[1,2,3,4,5,6]
t=11
print(sum(arr,t))



def sumi(a,b):
    r=[]
    for x in b:
        found=False
        for i in range(len(a)):
            for j in range(i+1,len(a)):
                if a[i]+a[j]==x:
                    found=True
                    break
            if found:
                break
        r.append(found)
    return r
            

a = [5, 7, 1, 2, 8, 4, 3]
b= [3, 20, 1, 2, 7]
print(sumi(a,b))