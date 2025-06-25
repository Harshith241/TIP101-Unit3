'''Write a function first_unique_char() that given a string my_str as a parameter, it finds the first non-repeating character in it and returns its index. If it does not exist, then return -1.

def first_unique_char(my_str):
    pass
Example Usage:

my_str = "leetcode"
print(first_unique_char(my_str))

str2 = "loveleetcode"
print(first_unique_char(str2))

str3 = "aabb"
print(first_unique_char(str3))
Example Output

0
2
-1'''


def first_unique_char(my_str): 
    char_count = {}
    for letter in my_str:
        if letter in char_count:
            char_count[letter] += 1
        else:
            char_count[letter] = 1

    for char in my_str:
        if char_count.get(char) == 1:
            return my_str.index(char)
    return -1
        
my_stri = "leetcode"
print(first_unique_char(my_stri))

str2 = "loveleetcode"
print(first_unique_char(str2))

str3 = "aabb"
print(first_unique_char(str3))
        
    




