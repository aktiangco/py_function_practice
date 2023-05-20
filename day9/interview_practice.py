# Activity: Interview Practice
# ! To check: python3 day9/interview_practice.py

'''
# * 1. Write an algorithm that checks if a string contains another string.

If it does, return True; otherwise, return False.
Example: When checking if string "Hello world" contains "Hello", the function should return True. If checking if the same string contains "Bye", the function should return False.
'''
def check_string(main, sub):
    if sub in main:
        return True
    else: 
        return False
    
main = "Hello World"
sub1 = "Hello"
sub2 = "bye"
print("1. ======")

print(f"Output: {check_string(main, sub1)}") # Output: True
print(f"Output: {check_string(main, sub2)}") # Output: False 

print("======\n")   



'''
# * 2. Write a recursive function that takes in a number and returns the sum of the numbers from 0 to the number.

Example: if the input is 5, the expected output would be 15 (5+4+3+2+1 = 15).
'''
def recursive(num):
    # base case
    if num == 1:
        return 1
    # recursive case
    else: 
        return (num + recursive(num-1)) 
n = 5
print("2. ======")

print(f"Output: {recursive(n)}") # Output: 15

print("======\n") 


'''
# * 3. Write a function that takes in a string and returns the string reversed.

Example: if the input is "hello", the expected output would be "olleh".
'''
def reverse_string(input):
    if  len(input) == 0:
        return ""
    else:
        return input[-1] + reverse_string(input[:-1])

input = "Hello"
reverse_string = reverse_string(input)
print("3. ======")

print(f"Output: {reverse_string}") # Output: olleH

print("======\n") 


'''
# * 4. Write a recursive function that takes in a list of strings and returns the words capitalized.

Example: if the input is ['pandas', 'monkeys', 'koalas', 'kangaroos'], then the expected output would be PANDAS MONKEYS KOALAS KANGAROOS.
'''
def capitalized(lst):
    if len(lst) == 0:
        return []
    else:
        return[lst[0].upper()] + capitalized(lst[1:])

input = ['pandas', 'monkeys', 'koalas', 'kangaroos']
capitalized = capitalized(input)

print("4. ======")

print(f"Output: {capitalized}") # Output: ['PANDAS', 'MONKEYS', 'KOALAS', 'KANGAROOS']

print("======\n") 

'''
# TODO: 5. Write a function that takes in a list of numbers and returns the product of the numbers in the list.

Example: if this input is [4, 3, 5], then the expected output would be 60 (4*3*5=60).
'''
def product(num):
    if len(num) == 0:
        return 1
    else:
        return num[0] * product(num[1:])
    
input = [4, 3, 5]
product = product(input)

print("5. ======")

print(f"Output: {product}") # Output: 60

print("======\n") 

'''
# * 6. Write an algorithm that prints the non-repeating integers in a list.

Example: in a list of [1, 5, 1, 6, 8, 5], the expected output would be 6, 8.
'''
def non_repeat(num_lst):
    count_dict = {}
    non_repeating_num = []
    print("6. =======")

    for num in num_lst:
        count_dict[num] = count_dict.get(num, 0) + 1

    for num, count in count_dict.items():
        if count == 1:
            non_repeating_num.append(num)

    for num in non_repeating_num:
        print(f"non repeated numbers: {num}")
    print("======")    

numbers = [1, 5, 1, 6, 8, 5]
non_repeat(numbers)
