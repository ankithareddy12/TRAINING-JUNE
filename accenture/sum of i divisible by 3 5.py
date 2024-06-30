'''The function accepts 2 positive integer ‘m’ and ‘n’ as its arguments.You are required to calculate the sum of numbers divisible both by 3 and 5, between ‘m’ and ‘n’ both inclusive and return the same.
Note'''
m=12
n=50
s=[]
for i in range(m,n+1):
    if i%3==0 and i%5==0:
        s.append(i)
print(sum(s))
        