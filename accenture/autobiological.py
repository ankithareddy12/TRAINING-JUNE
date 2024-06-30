'''Input:

n: “1210”

Output:

3

Explanation:

0th position in the input contains the number of 0 present in input, i.e. 1, in 1st position the count of number of 1s in input i.e. 2, in 2nd position the count of 2s in input i.e. 1, and in 3rd position the count of 3s i.e. 0, so the number is an autobiographical number.

Now unique numbers in the input are 0, 1, 2, so the count of unique numbers is 3. So 3 is returned.'''
n=1210
n=str(n)
print(n.count('0'),end="")
print(n.count('1'),end="")
print(n.count('2'),end="")
print(n.count('3'),end="")


def autobiographical_number_count(n):
    # Initialize a list to count occurrences of each digit (0-9)
    digit_counts = [0] * 10
    
    # Count occurrences of each digit in the number n
    temp = n
    while temp > 0:
        digit = temp % 10  # Extract the last digit
        digit_counts[digit] += 1  # Increment count for the digit
        temp //= 10  # Move to the next digit
    
    # Count the number of unique digits present
    unique_digit_count = 0
    for count in digit_counts:
        if count > 0:
            unique_digit_count += 1
    
    return unique_digit_count

# Example usage:
n = 1210
result = autobiographical_number_count(n)
print(f"Output: {result}")  # Output: 3



        
        