#create parenthesis:
"""def parenthesis(n):
    r=[]
    def fun(s,open_c,close_c):
        if len(s)==2*n:
            r.append(s)
            return
        elif open_c<n:
            fun(s+'(',open_c+1,close_c)
        elif close_c<open_c:
            fun(s+')',open_c,close_c+1)
    fun('',0,0)
    return r


print(parenthesis(3))

#valid parenthesis
def valid(s):
    r=[]
    for i in range(len(s)):
        if s[i]=='(':
            r.append(')')
        elif s[i]=='[':
            r.append(']')
        elif s[i]=='{':
            r.append('}')
        elif len(r)==0 or r.pop()!=s[i]:
            return False
    return len(r)==0
s="(){}("
print(valid(s))
"""
#valid parenthesis str
def valid(s):
    r=0
    for i in s:
        if i in '(*':
            r+=1
        else:
            r-=1
        if r<0:
            return False
    r=0
    for i in reversed(s):
        if i in '*)':
            r+=1
        else:
            r-=1
        if r<0:
            return False
    return True
s='*'
print(valid(s))
    
        
 #score of parenthesis       
        
        stack = [0]  # Stack to keep track of scores
        
        for char in s:
            if char == '(':
                stack.append(0)
            else:
                v = stack.pop()
                stack[-1] += max(2 * v, 1)
        
        return stack.pop()
            












