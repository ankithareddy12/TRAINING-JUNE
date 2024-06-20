#sum of integers

class Solution(object):
    def twoSum(self, numbers, target):
        l,r=0,len(numbers)-1
        
        while l<r:
            currSum=numbers[l]+numbers[r]
            if currSum>target:
                r-=1
            elif currSum<target:
                l+=1
            else:
                return [l+1,r+1]
            

def find_indices(s, t):
    i, j = 0, len(s) - 1  # Initialize pointers
    
    while i < j:
        curr_sum = s[i] + s[j]
        if curr_sum > t:
            j -= 1
        elif curr_sum < t:
            i += 1
        else:
            return True  # Return 1-indexed positions
    
    return False  # Return None if no pair is found

# Test the function
s = [1, 2, 3, 5, 6]
t = 5
result = find_indices(s, t)
print(result)


#3sum
class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        n = len(nums)
        result = []
        
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            left, right = i + 1, n - 1
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
        
        return result
    
#palindrome]
s = "race e car"
i = 0
j = len(s) - 1

while i < j:
    # Move `i` to the next alphanumeric character
    while i < j and not s[i].isalnum():
        i += 1
    # Move `j` to the previous alphanumeric character
    while i < j and not s[j].isalnum():
        j -= 1
    
    if s[i].lower() != s[j].lower():
        i += 1
        j -= 1
    else:
       print("False")
print("True")

#subsequnece
def is_subsequence(s, t):
    i, j = 0, 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
        j += 1
    return i == len(s)

# Example usage
s = "ade"
t = "abce"
print(is_subsequence(s, t))  # Output: True


#water
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        distance = right - left
        max_area = 0
        while left < right:
            max_area = max(min(height[left],height[right]) * distance, max_area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
            distance -= 1
        return max_area