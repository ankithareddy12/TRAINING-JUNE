
def paren(s):
    stack = []
    for char in s:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return False
            stack.pop()
    return not stack

str = ["(()))"]
results = [paren(s) for s in str]
print(results) 
def paren(s):
    stack = []
    matching = {')': '(', ']': '[', '}': '{'}
    
    for char in s:
        if char in matching.values():
            stack.append(char)
        elif char in matching.keys():
            if not stack or stack[-1] != matching[char]:
                return False
            
            
            stack.pop()
    return -1


strs = ["((()))"]
results = [paren(s) for s in strs]
print(results)  



def index(s):
    stack = []
    indices = []
    matching = {')': '(', ']': '[', '}': '{'}

    for i, char in enumerate(s):
        if char in matching.values():
            stack.append(char)
            indices.append(i)
        elif char in matching.keys():
            if not stack or stack[-1] != matching[char]:
                return i 
            stack.pop()
            indices.pop()

    if stack:
        return indices[-1]  

    return -1  

str = ["((())})"]
for s in str:
    unmatched_index = index(s)
    if unmatched_index == -1:
        print(" balanced.")
    else:
        print( {unmatched_index})






















