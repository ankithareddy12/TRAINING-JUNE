def fin_sub(s):
    sub=[]
    def generate(i,index):
        if index==len(s):
            sub.append(i)
            return
        generate(i+[s[index]],index+1)
        generate(i,index+1)
    generate([],0)
    return sub
s="Abc"
x=fin_sub(s)
print(x)