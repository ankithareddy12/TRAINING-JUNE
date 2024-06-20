n = 12
k = 5
f=[]
count = 0
for i in range(1, n+1):
    if n % i == 0:
        f.append(i)
        count += 1
        if count == k:
            print(i)
            
if count < k:
    print(-1)
print(f)   

#factors
number=15

factors = []
for i in range(1, number + 1):
    if number % i == 0:
        factors.append(i)
print(factors)
