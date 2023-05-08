# Activity: Python Tricks Practice
# *! To check: python3 day4/py_tricks.py

'''
#* TODO Write a lambda function to sort a list of tuples in ascending order according to the number in the second position of each tuple.
 - Unsorted list of tuples: [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)] Sorted list of tuples: [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]
'''
data = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)] # Unsorted List of tuples
sort_data = sorted(data, key=lambda data: data[1])

print(sort_data)
# Output: Sorted list of tuples: [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]
 
'''
#* TODO Write a lambda function to cube every element of a list.
 - Original list: [3,6,9,2] List after lambda function: [27,216,729,8]
'''
cube_nums = lambda x: [i**3 for i in x] # 
print(cube_nums([3,6,9,2])) # Output: [27, 216, 729, 8]


'''
#* TODO Write a lambda function to determine whether a number is even or odd (the function should return True or False), and then use the function and a list comprehension to create a new list of booleans, where even numbers are True and odd numbers are False.
 - Input list: [3,6,9,2] List after lambda function and list comprehension: [False, True, False, True]
'''
even = lambda x: x %2 == 0 # Check if numbers is even
numbers = [3,6,9,2] # Input list: [3,6,9,2] 
result = [even(num) for num in numbers]

print(result) # Output: [False, True, False, True]

#* from the solution code
#* much more simple
#* even_odd = lambda x: True if x%2 == 0 else False
#* print([even_odd(x) for x in [3,6,9,2]])

'''
#* TODO Use a list comprehension to create a list of the numbers from 1 to 100 (including 100)
'''
numbers = [num for num in range(1, 101)] #101 to include 100
print(numbers) # Output: [1, 2, 3 ... 100]

'''
#* TODO Use a dictionary comprehension to count the length of each word in a sentence.
 - Input: "The quick brown fox jumped over the fence." output: {'The': 3, 'quick': 5, 'brown': 5, 'fox': 3, 'jumped': 6, 'over': 4, 'the': 3, 'fence.': 6}
'''
sentence = "The quick brown fox jumped over the fence." # Input: "The quick brown fox jumped over the fence."
result = {word: len(word) for word in sentence.split()} # "len()" method check for the length oh the word, "split()" method splits a string into a list

print(result) # Output: {'The': 3, 'quick': 5, 'brown': 5, 'fox': 3, 'jumped': 6, 'over': 4, 'the': 3, 'fence.': 6}
