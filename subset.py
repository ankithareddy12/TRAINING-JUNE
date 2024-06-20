def generate_subsets(nums):
    def backtrack(start, subset):
        result.append(subset[:]) 
        for i in range(start, len(nums)):
            subset.append(nums[i]) 
            backtrack(i + 1, subset)
            subset.pop()  

    result = []
    backtrack(0, []) 
    return result

nums = [1, 2, 3]
print(generate_subsets(nums))

def generate_subsets(nums):
    def backtrack(start, subset):
        result.append(subset[:]) 
        for i in range(start, len(nums)):
            subset.append(nums[i]) 
            backtrack(i + 1, subset)
            subset.pop()  

    result = []
    backtrack(0, []) 
    return result

def sum_of_subsets(nums):
    subsets = generate_subsets(nums)
    
    subset_sums = [sum(subset) for subset in subsets]
    return subset_sums

nums = [1, 2, 3]
print(generate_subsets(nums))
print(sum_of_subsets(nums))
def generate_subsets(nums):
    def backtrack(start, subset):
        result.append(subset[:]) 
        for i in range(start, len(nums)):
            subset.append(nums[i]) 
            backtrack(i + 1, subset)
            subset.pop()  

    result = []
    backtrack(0, []) 
    return result

def sum_of_result(nums):
    subsets = generate_subsets(nums)
    result_sum = sum(map(sum, subsets))
    return result_sum

nums = [1, 2, 3]
print(generate_subsets(nums))
print(sum_of_result(nums))

