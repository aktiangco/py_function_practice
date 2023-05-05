# Activity: Python Function Fun Part 3
# *! To check: python3 day2/activity3.py

#* name_args - Accepts any number of named arguments and prints them in the pattern key : value one at a time.
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
def all_true(iterable):
    """
    Returns True if all the elements in an iterable are true.
    """
    # The all() function takes an iterable and returns True if all the elements are true, and False otherwise.
    # We can simply return the result of calling all() on the input iterable.
    return all(iterable)

print(all_true([True, True, False, True]))
# Output: False

print(all_true([1, 2, 3]))
# Output: True

print(all_true([]))
# Output: True

#* one_true - Returns True if one of the elements in an iterable is true. Hint: there is an existing built-in function that could be very helpful here.
def one_true(iterable):
    """
    Returns True if at least one element in the iterable is true.
    """
    return any(iterable)  # Uses the built-in 'any' function to check if at least one element is true

print(one_true([False, False, True]))
# Output: True

print(one_true([False, 0, None]))
# Output: False

#* recursive_factorial - Uses recursion to find the factorial of an integer.
def recursive_factorial(n):
    """
    Uses recursion to find the factorial of an integer.
    
    Parameters:
    n (int): the integer to find the factorial of
    
    Returns:
    int: the factorial of n
    
    Example:
    recursive_factorial(5) -> 120
    """
    if n == 0:
        return 1
    else:
        return n * recursive_factorial(n-1)

# calculate the factorial of 5
result = recursive_factorial(5)
print(result)
#  Output: 120

#* recursive_deduplicate - Recursively removes all adjacent duplicate letters from a string.
def recursive_deduplicate(s):
    """
    Recursively removes all adjacent duplicate letters from a string.

    Args:
    s (str): The string to remove adjacent duplicates from.

    Returns:
    str: The input string with adjacent duplicates removed.
    """
    # Base case: if the string is empty or has only one character, there are no adjacent duplicates to remove
    if len(s) < 2:
        return s

    # Recursive case: remove the adjacent duplicates from the substring after the first occurrence of the current character
    if s[0] == s[1]:
        return recursive_deduplicate(s[1:])
    else:
        return s[0] + recursive_deduplicate(s[1:])
print(recursive_deduplicate("AABBCCDD")) # Input: AABBCCDD
# Output: ABCD

#* recursive_reverse - Uses recursion to reverse a string.
def recursive_reverse(s):
    # base case: empty string or single character
    if len(s) <= 1:
        return s

    # recursive case: reverse the rest of the string and append the first character
    return recursive_reverse(s[1:]) + s[0]

s = 'hello world'
reversed_s = recursive_reverse(s)
print(reversed_s)  # prints 'dlrow olleh'