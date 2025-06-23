'''Write a function swap_ends() that accepts a string my_str as a parameter and returns a new string where the first and last characters from my_str are swapped.

def swap_ends(my_str):
    pass
Example Usage:

my_str = "boat"
swapped = swap_ends(my_str)
print(swapped)
Example Output: toab'''

def swap_ends(my_str):
    first_letter = my_str[0]
    middle_part = my_str[1:len(my_str) - 1]
    last_letter = my_str[len(my_str) - 1]
    return last_letter + middle_part + first_letter

my_stri = "boat"
swapped = swap_ends(my_stri)
print(swapped)