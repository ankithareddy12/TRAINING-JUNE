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
    c=0
    board=[['.' for _ in range(n)] for _ in range(n)]
    solve(board,0)
    return result
   

solutions = solveNQueens(4)
for solution in solutions:
    for row in solution:
        print(row)
    print()
