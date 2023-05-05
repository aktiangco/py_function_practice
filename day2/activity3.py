# Activity: Python Function Fun Part 3
# *! To check: python3 day2/activity3.py

#* name_args - Accepts any number of named arguments and prints them in the pattern key : value one at a time.
# TODO
def name_args(**kwargs):
    """
    Accepts any number of named arguments and prints them in the pattern key : value one at a time.
    """
    # loop through each key-value pair in the kwargs dictionary
    for key, value in kwargs.items():
        # print the key-value pair in the format "key : value"
        print(f"{key} : {value}")

name_args(name='Allan', age=35, city='Honolulu')


#* all_true - Returns True if all the elements in an iterable are true. Hint: there is an existing built-in function that could be very helpful here.
# TODO

#* one_true - Returns True if one of the elements in an iterable is true. Hint: there is an existing built-in function that could be very helpful here.
# TODO

#* recursive_factorial - Uses recursion to find the factorial of an integer.
# TODO

#* recursive_deduplicate - Recursively removes all adjacent duplicate letters from a string.
# Input: AABBCCDD
# Output: ABCD
# TODO

#* recursive_reverse - Uses recursion to reverse a string.
# TODO