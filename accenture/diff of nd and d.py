'''Implement the following Function 

def differenceofSum(n. m)

The function accepts two integers n, m as arguments Find the sum of all numbers
in range from 1 to m(both inclusive) that are not divisible by n. Return difference between sum of integers not divisible
by n with sum of numbers divisible by n.'''

def differenceofSum(n,m):
    c=0
    c1=0
    for i in range(1,m+1):
        if i%n==0:
            c=c+i      
        else:
            c1+=i  
            
    return abs(c1-c)

n=4
m=20
x=differenceofSum(n,m)
print(x)
    

        