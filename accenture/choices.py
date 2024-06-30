'''Int OperationChoices(int c, int n, int a , int b )

The function accepts 3 positive integers ‘a’ , ‘b’ and ‘c ‘ as its arguments. Implement the function to return.

( a+ b ) , if c=1
( a – b ) , if c=2
( a * b ) ,  if c=3
(a / b) ,  if c =4'''


a = 12
b = 16
c = 1

for choice in range(1, 5):
    if choice == c:
        if choice == 1:
            print(a + b)
        elif choice == 2:
            print(a - b)
        elif choice == 3:
            print(a * b)
        elif choice == 4:
            if b != 0:  # Check for division by zero
                print(a / b)
            else:
                print("Error: Division by zero")
        else:
            print("no")
def operationChoices(c,a,b):
    if c == 1 :
        return(a+b)
    elif c == 2:
        return(a-b)
    elif c == 3:
        return(a*b)
    else:
        return(a//b)
c,a,b = map(int,input().split())
print(operationChoices(c, a, b))