
    
def island(grid):
    if not grid:
        return 0
    def water(grid,row,col):
        rows=len(grid)
        cols=len(grid[0])
        if row<0 or row>=rows or col<0 or col>=cols or grid[row][col]==0:
             return 
        grid[row][col]=0
        water(grid,row-1,col)
        water(grid,row+1,col)
        water(grid,row,col-1)
        water(grid,row,col+1)
    island_count=0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]==1:
                island_count+=1
                water(grid,i,j)
    return island_count

       
    
grid=[[0,1,0,0,1],
        [1,0,0,1,1],
        [0,0,0,0,0],
        [1,0,0,0,0],
        [1,0,0,0,1]]

print(island(grid))
        
