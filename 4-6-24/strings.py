"""#print k characters from alphabet e back
n = "bvec"
m = 4
s = ""
for i in n:
    if m > ord(i) - ord('a'):
        s += chr(ord('z') - (m - (ord(i)-ord('a')) - 1))
    else:
        s += chr(ord(i)-m)
print(s)


def alpha(a,k):
    text=""
    for i in a:
        if 'a'<=i<='z':
            c=chr(((ord(i)-ord('a')-k)%26)+ord('a'))
        else:
            c=i
        text+=c
    return text
a = "bvec"
k = 4
text = alpha(a, k)
print(text)

a = "bvec"
k = 4
c=k%26
d=''
for i in a:
    if((ord(i)-c)>=97):
        d=d+chr(ord(i)-c)
    else:
        d=d+chr(ord(i)-c+26)
print(d)


def sub_string(s):
    if not s:
        return 0
    mx=1
    length=1
    for i in range(1,len(s)):
        if s[i]==chr(ord(s[i-1])+1):
            length+=1
        else:
            mx=max(mx,length)
            length=1
    mx=max(mx,length)
    return mx
s="xyzabcde"
r=sub_string(s)
print(r)
"""
"""
n = 3  # Size of the matrix (3x3 in this case)
matrix = []

# Fill the matrix with user input characters
for i in range(n):
    row = []
    for j in range(n):
        char = input(f'Enter character for position ({i+1},{j+1}): ')
        row.append(char)
    matrix.append(row)

# Print the filled matrix
for row in matrix:
    print(row)








"""

def printSubsequence(input, output):

    if len(input) == 2:
        print(output, end=' ')
        return
    printSubsequence(input[1:], output+input[0])
 
    printSubsequence(input[1:], output)

output = ""
input = "abcd"
 
printSubsequence(input, output)

def find_substrings_of_length_3(s):
    substrings = []
    for i in range(len(s) - 2):
  
        substrings.append(s[i:i+3])
    return substrings

string = "abcdef"
substrings = find_substrings_of_length_3(string)
print(substrings)  
















