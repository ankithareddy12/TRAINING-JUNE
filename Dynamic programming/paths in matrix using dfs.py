

def fun(i, j, c, visited):
    if i < 0 or i >= m or j < 0 or j >= n or (i, j) in visited: 
        return c
    if i == m - 1 and j == n - 1:
        c += 1
        return c

    visited.add((i, j))
    
    c = fun(i - 1, j, c, visited)  
    c = fun(i + 1, j, c, visited)  
    c = fun(i, j - 1, c, visited)  
    c = fun(i, j + 1, c, visited)  
    
    visited.remove((i, j))
    
    return c

m = 4
n = 3
c = 0
visited = set()
print(fun(0, 0, c, visited))
