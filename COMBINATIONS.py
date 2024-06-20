from itertools import combinations
input_string=input()
k=int(input())
i=0
sorted_string=sorted(input_string)
for i in range(i,k+1):
    for combo in combinations(sorted_string,i):
        print(''.join(combo))