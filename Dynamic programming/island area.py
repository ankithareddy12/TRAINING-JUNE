def island(grid):
    if not grid:
        return 0,0
    def water(grid,row,col):
        rows=len(grid)
        cols=len(grid[0])
        if row<0 or row>=rows or col<0 or col>=cols or grid[row][col]==0:
             return 0
        grid[row][col]=0
        area=1
        area+=water(grid,row-1,col)
        area+=water(grid,row+1,col)
        area+=water(grid,row,col-1)
        area+=water(grid,row,col+1)
        return area
    island_count=0
    max_area=0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]==1:
                island_count+=1
                
                max_area = max(max_area,water(grid,i,j))
    return island_count,max_area

       
    
grid=[[0,1,0,0,1],
        [1,0,0,1,1],
        [0,0,0,0,0],
        [1,0,0,0,0],
        [1,0,0,0,1]]


island_count,max_area=island(grid)
print(island_count)
print(max_area)



