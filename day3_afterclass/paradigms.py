# Activity: Reflecting on Coding Paradigms
# *! To check: python3 day3_afterclass/paradigms.py

#* Functional Prompt
''' 
Implement a function that will flatten and sort an array of integers in ascending order, and which adheres to a functional programming paradigm.

Remember, when writing in a functional style:
 - Keep variables immutable
 - Write only pure functions
 - Remember, functions may be higher order
'''
def flatten_and_sort(array):
    # Initialize an empty list to store flattened elements
    arr = []
    # Iterate through each element in the input array
    for item in array:
        # If the element is a list, iterate through its elements and append them to arr
        if isinstance(item, list):
            for i in item:
                arr.append(i)
        # If the element is not a list, append it directly to arr
        else:
            arr.append(item)
    # Return a new sorted list
    return sorted(arr)

#* Test 1
test = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
res = flatten_and_sort(test)
print(res)
# output: [1, 2, 3, 4, 5, 6, 7, 8, 9] 
#* Test 2
test2 = [[1, 6, 8], [5, 3, 7], [5, 2, 9]]
res2 = flatten_and_sort(test2)
print(res2)
# output: [1, 2, 3, 5, 5, 6, 7, 8, 9]
#* Test 3
test3 = [["a", "g", "n"], ["b", "t", "c"], ["f", "s", "z"]]
res3 = flatten_and_sort(test3)
print(res3)
# output: ['a', 'b', 'c', 'f', 'g', 'n', 's', 't', 'z']

'''
# TODO 
Once a functional solution to this problem has been implemented, answer the following questions.
 #? - How does this solution ensure data immutability?
    #* It creates a list without modifying the original input list, ensures input list remains unchanged.
 #? - Is this solution a pure function? Why or why not?
    #* This solution is pure because it has no side effects, is deterministic, and has no external dependencies.
 #? - Is this solution a higher order function? Why or why not?
    #* This solution is not a higher-order function because it neither takes functions as arguments nor returns functions as output.
 #? - Would it have been easier to solve this problem using a different programming style?
    #* 
 #? - Why in particular is functional programming a helpful paradigm when solving this problem?
    #* 
'''

#* Object Oriented Prompt
'''
#  TODO
Watto needs a new system for organizing his inventory of podracers. Help him do this by implementing an Object Oriented solution according to the following criteria.
 - First, he'll need a general Podracer class defined with max_speed, condition (perfect, trashed, repaired) and price attributes.
 - Define a repair() method that will update the condition of the podracer to "repaired".
 - Define a new class, AnakinsPod that inherits the Podracer class, but also contains a special method called boost that will multiply max_speed by 2.
 - Define another class that inherits Podracer and call this one SebulbasPod. This class should have a special method called flame_jet that will update the condition of another podracer to "trashed".
'''
# ? answer here


'''
# TODO
Once an Object Oriented solution has been implemented, answer the following questions:
 #? - How does this solution demonstrate the four pillars of OOP? (It may not demonstrate all of them, describe only those that apply)
    - Encapsulation
    - Abstraction
    - Inheritance
    - Polymorphism
 
 #? - Would it have been easier to implement a solution to this problem using a different coding style? Why or why not?
 
 #? - How in particular did Object Oriented Programming assist in the solving of this problem?

'''
# ? answer here