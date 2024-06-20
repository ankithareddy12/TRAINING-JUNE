"""str="hello:5438,car:214,book:8799,at:431"

pairs=str.split(',')
for pair in pairs:
    key, value=pair.split(':')
    length=len(key)
    print(length)
    if str(length) in value:
        char_index = int(value.index(str(length))) + 1
    else:
        char_index = int(length) % len(value)
        if char_index == 0:
            char_index = len(value)
    print(f"Length of {key} = {length}, character at index {char_index} = {value[char_index - 1]}")"""

inp = "hello:5438,car:214,book:8799,apple:2187"

def leng(x, y):
    xi = len(x)
    while xi not in map(int, str(y)):
        xi -= 1
        if xi < 1:
            return 0  
    return xi

s = ''
for i in inp.split(','):
    x, y = i.split(':')
    if str(len(x)) in str(y):
        s += x[len(x) - 1]
    else:
        length = leng(x, y)
        if length < 1:
            s += 'x'
        
        else:
            s+=x[length-1]

print(s)
