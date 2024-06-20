#1720,

"""n=[1,2,3]
first=1

a=[first]
for i in range(len(n)):
     a.append(n[i]^a[i])
  
print(a)

#2390
#remove *
s="leet**co*de"
lst=[]
for i in s:
    if i!='*':
        lst.append(i)
    else:
        lst.pop()
print(' '.join(lst))

#1859
s="is2 sentence4 This1 a3"
l=[]
for i in s.split(' '):
    l.insert(int(i[-1])-1,i[:-1])   
x=' '.join(l)
print(x)

#1929
nums = [1,2,1]
nums.extend(nums)
print(nums)

#1920
nums = [0,2,1,5,3,4]
ans = [nums[nums[0]], nums[nums[1]], nums[nums[2]], nums[nums[3]], nums[nums[4]], nums[nums[5]]]
print(ans)

#2011
  
def final_value_after_operations(operations):
    X = 0
    for operation in operations:
        if operation == "--X" or operation == "X--":
            X -= 1
        elif operation == "++X" or operation == "X++":
            X += 1
    return X

operations = ["--X", "X++", "X++"]
print(final_value_after_operations(operations)) 


#1512
def numIdenticalPairs(nums):
        pairs = 0
        d = {}
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        for num in d:
            val = d[num]
            for i in range(val):
                pairs += i
        return pairs
nums = [1,2,3,1,1,3]
print(numIdenticalPairs(nums))
    
       count, data = 0, {}
        for i in nums:
           data[i] = data.get(i, 0) + 1
            count += data[i]-1
        return count 

#1470
def shuffle(nums, n):
    result = []
    for i in range(n):
        result.append(nums[i])       # Append x_i
        result.append(nums[i + n])   # Append y_i
    return result

# Example usage:
nums = [2, 5, 1, 3, 4, 7]
n = 3
print(shuffle(nums, n))  # Output: [2, 3, 5, 4, 1, 7]

        
#2942
words = ["abc","bcd","aaaa","cbc"]
x = "a"
for index, i in enumerate(words):
    if x in i:
        print(index)
        

#2798
hours = [0,1,2,3,4]
target = 2
c=0
for i in hours:
    if i>=target:
        c+=1
print(c)
    
#1431
candies = [2,3,5,1,3]
extraCandies = 3
print(max(candies))
max=5
lst=[]
for i in candies:
    lst.append(i+extraCandies>=max)
print(lst)
    
#2824
nums = [-1, 1, 2, 3, 1]
target = 2
i = 0
c = 0

while i < len(nums) - 1:
    j = i + 1
    while j < len(nums):
        if nums[i] + nums[j] < target:
            c += 1
        j += 1
    i += 1

print(c)

#1365
def smaller_numbers_than_current(nums):
    result = []
    for i in range(len(nums)):
        count = 0
        for j in range(len(nums)):
            if nums[j] < nums[i]:
                count += 1
        result.append(count)
    return result

# Example usage:
nums = [8, 1, 2, 2, 3]
print(smaller_numbers_than_current(nums))  # Output: [4, 0, 1, 1, 3]


def smaller_numbers_than_current(nums):
    nums_sorted = sorted(nums)
    result = []

    for num in nums:
        count = nums_sorted.index(num)
        result.append(count)

    return result
nums = [8, 1, 2, 2, 3]
print(smaller_numbers_than_current(nums)) 

#31
class Solution(object):
    def nextPermutation(self, nums):
        i = len(nums) - 2
        while i >= 0 and (nums[i] >= nums[i+1]):
            i -= 1
        if i != -1:
            j = len(nums) - 1
            while j >= 0 and (nums[j] <= nums[i]):
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        nums[i+1:] = reversed(nums[i+1:])

#1480
nums = [1, 2, 3, 4]
running_sum = []
current_sum = 0
for num in nums:
    current_sum += num
    running_sum.append(current_sum)
print(running_sum)


#2114
sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
maxi=0
for i in sentences:
    print(i.split())
    n=len(i.split())
    maxi=max(maxi,n)
print(maxi)

#1389
nums = [0, 1, 2, 3, 4]
index = [0, 1, 2, 2, 1]
target = []

for i in range(len(nums)):
    target.insert(index[i], nums[i])

print(target)

#1313
nums = [1, 2, 3, 4]
output = []

for i in range(0, len(nums), 2):
    freq = nums[i]
    val = nums[i + 1]
    output.extend([val] * freq)

print(output)


#2974
nums=[5,4,2,3]
nums.sort()
for i in range(0,len(nums),2):
    nums[i],nums[i+1]=nums[i+1],nums[i]
print(nums)

#1662
word1 = ["ab", "c"]
word2 = ["a", "bc"]
word1=''.join(word1)
word2=''.join(word2)
if word1== word2:
    return True
else:
    return False

#1816
s = "Hello how are you Contestant"
k = 4
s=s.split()
print(" ".join(s[:k]))


#1773
class Solution:
    def countMatches(self, items,ruleKey,ruleValue):
        count=0
        if ruleKey=="type":
            j=0
        elif ruleKey=="color":
            j=1
        else:
            j=2
        for i in range(len(items)):
            if ruleValue==items[i][j]:
                count+=1
        return count
#1528
ans = ""
for i in range(len(indices)):
``` ans += s[indices.index(i)]
return ans
"""
#2108
#words = ["abc","car","ada","racecar","cool"]
#for i i words:
 #   if i=i

a='absba'
print(a[:-1])


    


























