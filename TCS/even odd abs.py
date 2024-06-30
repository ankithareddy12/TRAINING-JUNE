n=4567
n=str(n)
c=0
c1=0

for i in range(len(n)):
   
    if i%2==0:
        c=c+int(n[i])
        
    else:
        c1=c1+int(n[i])
        
print(c)
print(c1)
print(c1-c)
