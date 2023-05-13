# Activity: Calculating Big O
# *! To check: python3 day7/big_o.py

list_of_values = ['a', 'b', 'c', 'd', 'e']
# function 1
def function1(values):
  for value in values:
    print(value)

# function 2
def function2(values):
  print(values[0])
  print(values[1])

# function 3
def function3(values):
  for x in values:
    for y in values:
      print(x, y)

# function 4
def function4(values):
  for i in range(4): #O(n)
    print("Python is great")
  
    #O(1)
  print("Software Engineering is awesome!")
  print("Software Engineering is awesome!")
   
    #O(n)
  for value in values:
    print(value)
   
    #O(n)
  for value in values:
    print(value)

# It may be helpful to comment out all of the functions beside the function you are focusing on. This can help with determining the output of the function you are analyzing.

function1(list_of_values)
function2(list_of_values)
function3(list_of_values)
function4(list_of_values)



def function5(n):
  test_list=[]

  for num in range(n):
    test_list.append('add me')

  return test_list

print(function5(3))
print(function5(4))
print(function5(5))



# # example 
# sample_list = ['chocolate', 'cotton candy', 'ice cream', 'brownies', ' fried doughs']

# def constantFct(test_list):
#     print(test_list[0])
    
# constantFct(sample_list)

# sample_list2 = [1, 2, 5]
# def quad(test_list):
#     for a in test_list:
#         for b in test_list:
#             print(a, b)
# quad(sample_list2)

def sum_list(num_list):
    sum_list = 0  # Initialize a variable to store the sum, starting from 0
    for i in num_list:  # Iterate through each element in the input list
        sum_list = sum_list + i  # Add the current element to the running sum
    return sum_list  # Return the final sum

print(sum_list([1, 2, 3]))  # Call the function with the list [1, 2, 3]
