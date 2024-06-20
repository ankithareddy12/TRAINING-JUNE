#1.How do you reverse a string?
def reverse_string(s):
    return s[::-1]
str="jeshu"
reversed_str=reverse_string(str)
print(reversed_str)

#2.How can you check whether a string is a palindrome or not?
def palindrome(s):
    string=s.replace(" ","").lower()
    return string == string[::-1]
str1="i love you "
print(palindrome(str1))

#3.How can you compute the number of numericals in a string?
def compute(s):
    c=sum(1 for char in s if char.isdigit())

    return c
str="I love you 143"
print(compute(str))

#4.How do you find the count for the occurrence of a particular character in a string?
def compute(s):
    char= "u"
    return s.count(char)
str="I love you 143"
print(compute(str))

#5.How do you find the non-matching characters in a string?
def find_non_matching_characters(s, chars_to_match):
    return [char for char in s if char not in chars_to_match]

# Example usage
s = "Hello, world!"
chars_to_match = "lo, "
non_matching_chars = find_non_matching_characters(s, chars_to_match)
print(non_matching_chars)  # Output: ['H', 'e', 'w', 'r', 'd', '!']

#5.How do you find out if the two given strings are anagrams?
def anagram(s1,s2):
    return sorted(s1)==sorted(s2)
s1="listen"
s2="silent"
print(anagram(s1,s2))

#6.How do you calculate the number of vowels and consonants in a string?
vowels=['a','e','i','o','u']
word='ankitha'
c=0
for character in word:
    if character in vowels:
        c+=1
print(c)

        
#consonants

vowels=['a','e','i','o','u']
c1=0
for character in word:
    if character not in vowels:
        c1+=1
word='ANKITHA'
print(c1)

#7.How do you reverse an array?
arr=[1,2,3,4,6]
rev=arr[::-1]
print(rev)

#8.How do you find the maximum element in an array?
print(max(arr))

#9.How do you total all of the matching integer elements in an array?
arr=[1,2,3,4,6,7,8,9,0]
match=[2,4,6]
c=0
for num in arr:
    if num in match:
        c+=1
print(c)