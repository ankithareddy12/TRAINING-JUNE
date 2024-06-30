'''The algorithm to find the number with maximum exponent of 2 between the given range is

Loop between ‘a’ and ‘b’. Let the looping variable be ‘i’.
Find the exponent (power) of 2 for each ‘i’ and store the number with maximum exponent of 2 so faqrd in a variable , let say ‘max’. Set ‘max’ to ‘i’ only if ‘i’ has more exponent of 2 than ‘max’.
Return ‘max’.'''
def exponent(a,b):
    m=[]
    x=0
    while True:
       
        value=2**x
        if value>b:

            break
        if value>=a:
            m.append(x)
        x+=1
    return m
            
    
a=7
b=12
x=exponent(a,b)
print(x)


a=7
b=12
mx=-1
for i in range(a,b+1):
    x=0
    
    while i%2==0:
        i//=2
        x+=1
    if x>mx:
        mx=x
print(2**mx)


















