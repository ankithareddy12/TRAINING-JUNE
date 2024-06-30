'''Problem: Write a program in C to display the table of a number and print the sum of all the multiples in it.

Test Cases:

Test Case 1:
Input:
5
Expected Result Value:
5, 10, 15, 20, 25, 30, 35, 40, 45, 50
275'''
n=5
sum=0
for i in range(1,11):
    x=n*i
    sum=sum+x
print(sum)