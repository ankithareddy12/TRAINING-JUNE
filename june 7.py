
lst=[0,5,3,6,4,2,1]
n = len(lst)
expected_sum = n*(n + 1) // 2 
actual_sum = sum(lst)  
miss = expected_sum - actual_sum
print(miss)

        