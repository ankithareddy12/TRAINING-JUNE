def checkPassword(s):
    
    u=0
    d=0
    p=0
    if len(s)>=4:
        if s[0].isdigit():
                return 0
        for i in s:
            
            if i=='/' or i==" ":
                return 0
            elif i.isupper():
                u+=1
            elif i.isdigit():
                d+=1
            elif i=='_' or i=='@' or i!='$':
                p+=1
            else:
                return 0
        if u>=1 and d>=1 and p>=1 :
            return 1
        else:
            return 0
    else:
        return 0
#s="aA1_67"
s="a987 abC012"
x=checkPassword(s)
print(x)
    
        
       
                
    