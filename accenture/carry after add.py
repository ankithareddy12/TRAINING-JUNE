'''A carry is a digit that is transferred to left if sum of digits exceeds 9 while adding two numbers from right-to-left one digit at a time

You are required to implement the following function.

Int NumberOfCarries(int num1 , int num2);

The functions accepts two numbers ‘num1’ and ‘num2’ as its arguments. You are required to calculate and return  the total number of carries generated while adding digits of two numbers ‘num1’ and ‘ num2’'''

def total_carry(n1,n2):
    c=0
    c1=0
    while n1>0 and n2>0:
        d1=n1%10
        d2=n2%10
        total=d1+d2+c
        if total>=10:
            c+=1
            c1+=1
        else:
            c=0
        n1//=10
        n2//=10
    return c1
    
n1=451
n2=349
x=total_carry(n1,n2)
print(x)
    