'''1. The program will recieve 3 English words inputs from STDIN

These three words will be read one at a time, in three separate line
The first word should be changed like all vowels should be replaced by *
The second word should be changed like all consonants should be replaced by @
The third word should be changed like all char should be converted to upper case
Then concatenate the three words and print them
Other than these concatenated word, no other characters/string should or message should be written to STDOUT

For example if you print how are you then output should be h*wa@eYOU.

You can assume that input of each word will not exceed more than 5 chars

Test Cases
Case 1
Input

how
are
you
Expected Output : h*wa@eYOU'''

n1='how'
n2='are'
n3='you'
v='aeiou'
x=[]
for i in n1:
    if i not in v:
        x.append(i)
    else:
        i="*"
        x.append(i)
print(x)
for i in n2:
    if i not in v:
        i='@'
        x.append(i)
    else:
        
        x.append(i)
print(x)
n3=n3.upper()
print(n3)
x=''.join(x)+''+n3
print(x)