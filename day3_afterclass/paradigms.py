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

#* Testing
test = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
res = flatten_and_sort(test)
print(res) # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9] 

test2 = [[1, 6, 8], [5, 3, 7], [5, 2, 9]]
res2 = flatten_and_sort(test2)
print(res2) # Output: [1, 2, 3, 5, 5, 6, 7, 8, 9]

test3 = [["a", "g", "n"], ["b", "t", "c"], ["f", "s", "z"]]
res3 = flatten_and_sort(test3)
print(res3) # Output: ['a', 'b', 'c', 'f', 'g', 'n', 's', 't', 'z']

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
Watto needs a new system for organizing his inventory of podracers. Help him do this by implementing an Object Oriented solution according to the following criteria.
 - First, he'll need a general Podracer class defined with max_speed, condition (perfect, trashed, repaired) and price attributes.
 - Define a repair() method that will update the condition of the podracer to "repaired".
 - Define a new class, AnakinsPod that inherits the Podracer class, but also contains a special method called boost that will multiply max_speed by 2.
 - Define another class that inherits Podracer and call this one SebulbasPod. This class should have a special method called flame_jet that will update the condition of another podracer to "trashed".
'''
 # - First, he'll need a general Podracer class defined with max_speed, condition (perfect, trashed, repaired) and price attributes.
class Podracer:
    def __init__(self, max_speed, condition, price):
        self.max_speed = max_speed
        self.condition = condition
        self.price = price
    
    # - Define a repair() method that will update the condition of the podracer to "repaired".
    def repair(self):
        self.condition = "repaired"
        
#  - Define a new class, AnakinsPod that inherits the Podracer class.
class AnakinsPod(Podracer):
    def __init__(self, max_speed, condition, price):
        super().__init__(max_speed, condition, price) # "super()" built-in function that allows a class to refer to its parent class
    # special method called boost that will multiply max_speed by 2
    def boost(self):
        self.max_speed *= 2   # "*=" multiple 
        
# - Define another class that inherits Podracer and call this one SebulbasPod.
class SebulbasPod(Podracer):
    def __init__(self, max_speed, condition, price):
        super().__init__(max_speed, condition, price)
    # special method called flame_jet that will update the condition of another podracer to "trashed
    def flame_jet(self, other):
        other.condition = "trashed"
        
#* Testing
# Create an instance of AnakinsPod
anakin_pod = AnakinsPod(max_speed=100, condition="perfect", price=1000)

# Create an instance of SebulbasPod
sebulba_pod = SebulbasPod(max_speed=80, condition="perfect", price=800)

# Call the boost method on AnakinsPod
anakin_pod.boost()
print(f"Anakin has utilized his boost to catch up with Sebulda and is now reaching a speed of {anakin_pod.max_speed}mph" ) # Output: Anakin has utilized his boost to catch up with Sebulda and is now reaching a speed of 200mph.

# Call the flame_jet method on SebulbasPod, passing in AnakinsPod as an argument
sebulba_pod.flame_jet(anakin_pod)
print(f"Sebulda {anakin_pod.condition} Anakin's Pod racer") # Output: Sebulda trashed Anakin's Pod racer

# Call the repair method on AnakinsPod
anakin_pod.repair()
print(f"Anakin's Pod racer has been {anakin_pod.condition}") # Output: Anakin's Pod racer has been repaired


'''
Once an Object Oriented solution has been implemented, answer the following questions:
 #? - How does this solution demonstrate the four pillars of OOP? (It may not demonstrate all of them, describe only those that apply)
    - Encapsulation
    - Abstraction
    - Inheritance
    - Polymorphism
    #* The OOP solution demonstrates the pillars of Encapsulation, Abstraction, Inheritance, and Polymorphism. Encapsulation is shown through the use of class methods and attributes, Abstraction through the hiding of internal implementation details, Inheritance through the creation of subclasses, and Polymorphism through the ability to use the same method on different objects with different results
 #? - Would it have been easier to implement a solution to this problem using a different coding style? Why or why not?
    #* Depending on the particular issue and the programmer's expertise with various coding styles, it may or may not have been simpler to create a solution to this problem using a different coding style.
 #? - How in particular did Object Oriented Programming assist in the solving of this problem?
    #* By offering a method to group related information and actions into classes and objects, enabling the encapsulation and abstraction of implementation specifics, and promoting code reuse through inheritance and polymorphism, OOP helped to solve this issue.
'''

