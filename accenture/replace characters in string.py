'''The function accepts a string  ‘ str’ of length n and two characters ‘ch1’ and ‘ch2’ as its arguments . Implement the function to modify and return the string ‘ str’ in such a way that all occurrences of ‘ch1’ in original string are replaced by ‘ch2’ and all occurrences of ‘ch2’  in original string are replaced by ‘ch1’.'''

def replace(s,ch1,ch2):
    n=len(s)
    s=s.replace(ch1,'#')
    
    s=s.replace(ch2,ch1)
   
    s=s.replace('#',ch2)
    return s
    
s="apples"
ch1="a"
ch2="p"
x=replace(s,ch1,ch2)
print(x)