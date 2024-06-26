# Given two strings, the first being a random string and the second being the same as the first, but with three added characters somewhere in the string (three same characters),

# Write a function that returns the added character

# E.g
# string1 = "hello"
# string2 = "aaahello"

# // => 'a'
# The above is just an example; the characters could be anywhere in the string and string2 is actually shuffled.

# Another example
# string1 = "abcde"
# string2 = "2db2a2ec"

# // => '2'
# Note that the added character could also exist in the original string

# string1 = "aabbcc"
# string2 = "aacccbbcc"

# // => 'c'
# You can assume that string2 will aways be larger than string1, and there will always be three added characters in string2.

# def solution(str1, str2):
#     char_count = {}
#     for char in str1:
#         if char in char_count.keys():
#             char_count[char] += 1
#     for char in str2:
#         if char not in char_count.keys():
#             char_count[char] += 1



def solution(string1,string2):
    char_count = {}
    for char in string1:
        if char in char_count.keys():
            char_count[char] += 1
        else:
            char_count[char] = 1
    for char in string2:
        if char not in char_count.keys():
            return char
        else:
            char_count[char] -= 1
    for char, count in char_count.items():
        if count < 0:
            return char
    
    