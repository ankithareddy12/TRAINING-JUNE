#merge sort
"""def merge_arr(nums1,num2):
    x=[]
    i,j=0,0
    while i<m and j<n:
        if nums1[i]<nums2[j]:
            x.append(nums1[i])
            i+=1
        else:
            x.append(nums2[j])
            j+=1
    while i<m:
        x.append(nums1[i])
        i+=1
    while j<n:
        x.append(nums2[j])
        j+=1
    return x
nums1 = [1,2,3]
nums2 = [2,5,6]
m=3
n=3
x=merge_arr(nums1,nums2)
print(x)
            
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        i = m - 1
        j = n - 1
        k = m + n - 1
        
        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
 nums = [3,2,3]
print(sorted(nums))
print(nums(len(nums)/2])


#remove element
nums=[0,1,2,2,3,0,4,2]
k=2
i=0
c=0
while i<len(nums):
    if nums[i]==k:
        nums.pop(i)
        i+=1
        
    else:
        print(nums[i],end=" ")
        c+=1
        i+=1

print(c)

#remove duplicates:
 while val in nums:
   nums.remove(val)
 return len(nums)
#
nums=[1,1,2,1,3,1,3]
i=2
while i<len(nums):
    if nums[i]==nums[i-2]:
        nums.pop(i)
    else:
        i+=1
print(nums)
#if 2 1,1 okay but no 3
k = 0
for i in nums:
            
     if k < 2 or i != nums[k - 2]:
         nums[k] = i
         k += 1
print(k)       
#class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 1
        for i in range(1, len(nums)):
            if j == 1 or nums[i] != nums[j - 2]:
                nums[j] = nums[i]
                j += 1
        return j
    
#rotate left
def rotate_array_right(arr, k):
    n = len(arr)
    k = k % n  
    arr[:] = arr[-k:] + arr[:-k]  


my_array = [1, 2, 3, 4, 5]
rotate_array_right(my_array, 2)
print(my_array) 

#rotate right
def rotate_array_right(arr, k):
    n = len(arr)
    k = k % n  
    arr[:] = arr[k:] + arr[:k]  


my_array = [1, 2, 3, 4, 5]
rotate_array_right(my_array, 2)
print(my_array)"""

#left
arr=[1,2,3,4,5]
i=0
k=2
n=len(arr)
k=k%n
arr[:]=arr[k:]+arr[:k]
print(arr)
#right
arr=[1,2,3,4,5,6,7]
i=0
k=2
n=len(arr)
k=k%n
arr[:]=arr[-k:]+arr[:-k]
print(arr)

class Solution:
    def rotate(self, nums,k) :
        """
        Do not return anything, modify nums in-place instead.
        """
        k=k%len(nums)
        l,r=0,len(nums)-1
        while l<r:
            nums[l],nums[r]=nums[r],nums[l]
            l+=1
            r-=1
        l,r=0,k-1
        while l<r:
            nums[l],nums[r]=nums[r],nums[l]
            l+=1
            r-=1
        l,r=k,len(nums)-1
        while l<r:
            nums[l],nums[r]=nums[r],nums[l]
            l+=1
            r-=1

        




       
