"""word = "abBCab"
c=0
word=set(word)
print(word)
for i in word:
    if i.isalpha() and i.islower() and i.upper() in set(word):
        c+=1
print(c)"""
#3121
word = "aaAbcBC"
c=0
a=''
for i in word:
    if i.islower() and i not in a  and i.upper()  in word:
            a=a+i
            if word.rindex(i)<word.index(i.upper()):
                c+=1
print(c)
a='a'
print(a.center(9,'_'))
