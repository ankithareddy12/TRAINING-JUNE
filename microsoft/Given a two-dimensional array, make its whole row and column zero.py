#Given a two-dimensional array, if any element within is zero, make its whole row and column zero.
def matrix(a,r,c):
    rows=len(a)
    cols=len(a[0])
    dp = [[a[i][j] for j in range(cols)] for i in range(rows)]
    
    ro=set()
    co=set()
    for i in range(rows):
        for j in range(cols):
            if a[i][j]==0:
                ro.add(i)
                co.add(j)
    
    for i in range(rows):
        for j in range(cols):
            if i in ro or j in co:
                dp[i][j]=0
    return dp
                
    
a=[[1,2,3],
   [9,4,7],
   [1,0,5],]
r=3
c=1
x=matrix(a,r,c)
for rows in x:
    print(rows)