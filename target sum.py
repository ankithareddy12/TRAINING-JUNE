
def find_target_sum_recursive(arr, target_sum, current_sum=0, index=0, current_combination=[], result=[]):
    if current_sum == target_sum:
        result.append(list(current_combination))
    
    if current_sum > target_sum or index >= len(arr):
        return
    
    current_combination.append(arr[index])
    find_target_sum_recursive(arr, target_sum, current_sum + arr[index], index + 1, current_combination, result)
    current_combination.pop()  
    
    find_target_sum_recursive(arr, target_sum, current_sum, index + 1, current_combination, result)

    return result

arr = [2, 3, 4, 5]
target = 11
result = find_target_sum_recursive(arr, target)
print(result)
