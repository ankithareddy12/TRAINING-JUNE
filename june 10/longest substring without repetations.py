
"""ip "abfgresagtyuiofde"
op
 7,9,12
 high 12 print 12"""


a = "abfgresagtyuiofde"
d={}
maxl=0
c=0
for char in a:
    if char not in d:
        d[char]=char
        c+=1
    else:
        if c>maxl:
            maxl=c
print(len(d))

def rec(a, d=None, maxl=0, c=0):
    if d is None:
        d = {}
    for char in a:
        if char not in d:
            d[char] = char
            c += 1
        else:
            if c > maxl:
                maxl = c
            d.clear()
            d[char] = char
            c = 1
    if c > maxl:
        maxl = c
    return maxl

n = "abfgresagtyuiofds"
x = rec(n)
print(x)


def longest_unique_substring_length(s):
    char_index_map = {}
    max_length = 0
    start = 0

    for end in range(len(s)):
        if s[end] in char_index_map:
            start = max(start, char_index_map[s[end]] + 1)
        char_index_map[s[end]] = end
        max_length = max(max_length, end - start + 1)

    return max_length

n = "abfgresagtyuiofde"

print(longest_unique_substring_length(n))
'


