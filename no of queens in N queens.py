def solveNQueens(n):
    def is_valid(board,row,col):
        
                
        for i in range(row):
            if board[i][col]=='Q':
                return False
        for i, j in zip(range(row-1,-1,-1),range(col-1,-1,-1)):
            if board[i][j]=='Q':
                return False
        for i, j in zip(range(row-1,-1,-1),range(col+1,n)):
            if board[i][j]=='Q':
                return False
        return True

    def solve(board,row):
        if row==n:
            result.append([''.join(row) for row in board])
            return
        for col in range(n):
            if is_valid(board,row,col):
                board[row][col]='Q'
                solve(board,row+1)
                board[row][col] = '.'


    result=[]
    board=[['.' for _ in range(n)] for _ in range(n)]
    solve(board,0)
    for i in result:
        c=0
        for j in i:
            c+=j.count('Q')
            print(j)
            
    print(c)
  
solveNQueens(6)
