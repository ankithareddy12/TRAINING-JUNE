'''You are required to input the size of the matrix then the elements of matrix, then you have to divide the main matrix in two sub matrices (even and odd) in such a way that element at 0 index will be considered as even and element at 1st index will be considered as odd and so on. then you have sort the even and odd matrices in ascending order then print the sum of second largest number from both the matrice'''
m=int(input())
arr=list(map(int,input().split()))
print(arr)
e=[]
o=[]
for i in range(m):
    if i%2==0:
        e.append(arr[i])
    else:
        o.append(arr[i])
print(sorted(e))
print(sorted(o))
print(sorted(e)[-2]+sorted(o)[-2])