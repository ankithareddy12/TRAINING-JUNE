n=2
print(bin(n)[2:])
r=[]
for i in range(n+1):
    r.append(bin(i)[2:].count("1"))
print(r)
    

def int_to_bin_manual(n):
    if n == 0:
        return "0"
    binary_str = ""
    while n >0:
        binary_str = str(n % 2) + binary_str
        n = n // 2
    return binary_str

number = 42
binary_representation = int_to_bin_manual(number)
print(binary_representation)  


def count_bits(n):
    result = []
    for i in range(n + 1):
        result.append(bin(i).count('1'))
    return result

n = 5
output = count_bits(n)
print(output)  
