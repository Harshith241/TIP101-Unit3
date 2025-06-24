'''Write a function reverse_string() that takes a string my_str as a parameter and returns the string reversed.

def reverse_string(my_str):
    pass
Example Usage:

my_str = "live"
print(reverse_string(my_str))
Example Output: evil'''

def reverse_string(my_str):
    rev_str = ""
    for i in range(len(my_str) - 1, -1, -1):
        rev_str += my_str[i]
    return rev_str


my_stri = "live"
print(reverse_string(my_stri))   

