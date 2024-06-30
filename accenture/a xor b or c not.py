'''Problem Description :
The Binary number system only uses two digits, 0 and 1 and number system can be called binary string.
You are required to implement the following function:

int OperationsBinaryString(char* str);

The function accepts a string str as its argument. The string str consists of binary digits eparated with an alphabet as follows:

– A denotes AND operation
– B denotes OR operation
– C denotes XOR Operation
You are required to calculate the result of the string str, scanning the string to right taking one opearation at a time,
and return the same.'''



def str(s):
    if s is None:
        return -1
    r=int(s[0])
    i=1
    while i<len(s):
        op=s[i]
        num=int(s[i+1])
        if op=='A':
            r=r&num
        elif op=='B':
            r=r|num
        else:
            r=r^num
        i+=2
    return r


s="1C0C1C1A0B1"
x=str(s)
print(x)














