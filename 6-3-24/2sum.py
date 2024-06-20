def twoSum( nums, target):
    i,j,sum=0,0,0
    c=0
    while i<len(nums) and j<len(nums):
        sum=nums[i]+nums[j]
        if sum==target:

            return [i,j]
            c+=1
            return c
        elif sum>target:
            j-=1
        elif sum<target:
            i+=1
nums = [2,7,11,15]
print(c)
target = 9
x=twoSum(nums,target)


        