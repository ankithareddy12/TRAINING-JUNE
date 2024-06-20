
"""def fun(d, start, visited=None):
    if visited is None:
        visited = []
    if start not in visited:
        visited.append(start)
        for i in d.get(start, []):
            fun(d, i, visited)
    return visited

d = {5: [7, 3], 7: [5, 4, 3], 4: [7, 8, 2], 8: [3, 4, 2], 3: [5, 7, 8], 2: [4, 8]}

visited_nodes = fun(d, 5)
print(visited_nodes)

#paths

def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph:
        return []
    paths = []
    for node in graph[start]:
        if node not in path:  
            new_paths = find_all_paths(graph, node, end, path)
            for p in new_paths:
                paths.append(p)
    return paths

d = {
    5: [7, 3],
    7: [5, 4, 3],
    4: [7, 8, 2],
    8: [3, 4, 2],
    3: [5, 7, 8],
    2: [4, 8]
}

paths = find_all_paths(d, 5, 2)
for path in paths:
    print(path)
    """
print("all paths")

#all paths of graph
def fun(d,x):
    l.append(x)
    if(x==2):
        print(l)
        l.pop()
        return
    for i in d[x]:
        if(i not in l):
            fun(d,i)
    l.pop()
d={5:[7,3],7:[5,4,3],4:[7,8,2],8:[3,4,2],3:[5,7,8],2:[4,8]}
l=[]
fun(d,5)
    
print()
print("costs of all paths")

#costs of all paths
def fun(d,x,cost=0,path_cost=0):
    l.append(x)
    if(x==2):
        print(l,path_cost)
        l.pop()
        return
    for i,cost in d[x]:
        if(i not in l):
            fun(d,i,cost+1,path_cost+cost)
    l.pop()
d={5:[(7,1),(3,2)],7:[(5,1),(4,5),(3,4)],4:[(7,5),(8,6),(2,7)],8:[(3,3),(4,6),(2,8)],3:[(5,2),(7,4),(8,3)],2:[(4,7),(8,8)]}
l=[]
fun(d,5)


#shortest path and shortest cost

print()
print("shortedt path and shortedt cost")
def fun(d,x,cost=0,path_cost=0,short_path=[],short_cost=float('inf')):
    l.append(x)
    if(x==2):
        if path_cost<short_cost:
            short_path=list(l)
            short_cost=path_cost
        
        l.pop()
        return short_path,short_cost
    for i,cost in d[x]:
        if(i not in l):
            short_path,short_cost=fun(d,i,cost+1,path_cost+cost,short_path,short_cost)
    l.pop()
    return short_path,short_cost
d={5:[(7,1),(3,2)],7:[(5,1),(4,5),(3,4)],4:[(7,5),(8,6),(2,7)],8:[(3,3),(4,6),(2,8)],3:[(5,2),(7,4),(8,3)],2:[(4,7),(8,8)]}
l=[]
short_path, short_cost=fun(d,5)
if short_path:
    print(short_path,short_cost)
else:
    print("No path found.")
