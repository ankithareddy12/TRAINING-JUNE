"""* * * * * 
* * * * * 
* * * * * 
* * * * * 
* * * * * 
n=5
for i in range(n):
    for j in range(n):
        print("*",end=" ")
    print()
    
* * * * * 
  * * * * 
    * * * 
      * * 
        * 
n=5
for i in range(n):
    for j in range(i):
        print(" ",end=" ")
    for j in range(i,n):
        print("*",end=" ")
    print()
 # to display stars in equilateral triangular form\
     * 
    * * 
   * * * 
  * * * * 
n=5
for i in range(1,5):
    print(' '*n,end=' ')
    print('* '*(i))
    n-=1
    *
   ***
  *****
 *******
*********    
    
n=5
for i in range(1,n+1):
    print(' '*(n-i) + '*' *(2*i-1))
*********
 *******
  *****
   ***
    *
n=5
for i in range(n,0,-1):
    print(' '*(n-i) + '*' *(2*i-1))

    *
   ***
  *****
 *******
*********
*********
 *******
  *****
   ***
    *
n=5
for i in range(1,n+1):
    print(' '*(n-i) + '*' *(2*i-1))   
n=5
for i in range(n,0,-1):
    print(' '*(n-i) + '*' *(2*i-1))
*****
*   *
*   *
*   *
*****
n=5
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1:
            print('*',end='')
        else:
            print(" ",end='' )
    print()
            """






