def fin_sub(s):
    sub=[]
    def generate(s,index,path):
        if index==len(s):
            sub.append("".join(path))
            return
        path.append(s[index])
        generate(s,index+1,path)
        path.pop()
        generate(s,index+1,path)
    generate(s,0,[])
    return sub
s="Abc"
x=fin_sub(s)
print(x)
