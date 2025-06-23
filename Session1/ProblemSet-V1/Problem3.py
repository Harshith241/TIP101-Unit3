'''Write a function is_pangram() that takes in a string my_str as a parameter and returns True if the string is a pangram and False if not. A pangram is a sentence containing every letter in the English alphabet.

def is_pangram(my_str):
    pass
Example Usage:

my_str = "The quick brown fox jumps over the lazy dog"
print(is_pangram(my_str))

str2 = "The dog jumped"
print(is_pangram(str2))
Example Output:

True
False'''

import string

def is_pangram(my_str):
    alpha = set(string.ascii_lowercase)
    char_str = set()
    for letter in my_str:
        if letter.lower() in alpha:
            char_str.add(letter.lower())
    
    if char_str == alpha:
        return True
    else:
        return False
    


my_stri = "The quick brown fox jumps over the lazy dog"
print(is_pangram(my_stri))

str2 = "The dog jumped"
print(is_pangram(str2))
