# Function Definition Practice:
# Define functions according to the following prompts. Run the Replit to verify correct output.

# 1. Function that accepts no arguments. It's called say_hello and returns nothing, just prints 'hello'.
def say_hello():
  print("hello")
say_hello()

# 2. a 'sum' function that accepts two integers and returns the sum.
def sum(x,y):
  return x + y
print(sum(5,10))

# 3. an 'average' function that accepts two numbers and returns the average.
def average(x,y):
  avg= (x + y)/2
  return avg

print(average(4,6))
  

# 4. A function that accepts a first name and a last name and formats it to "{last_name}, {first_name}" (returns a string)
def persons_name(first_name, last_name):
  return f"hello {last_name}, {first_name}, welcome to CSULB"
print(persons_name('marlon', 'baker'))

# 5. A function that accepts a first name, last name, graduation year, and student number and returns those four items together in a list.
def student_info(first_name, last_name, graduation_year, student_number):
  return [first_name, last_name, graduation_year, student_number]
print(student_info('allan', 'tiangco', 2023, 163204))


# 6. A function that accepts an integer and returns whether it is above 18 or not (Boolean).
def over_18(num):
  if num > 18:
    return True
  else:
    return False

print(over_18(21))
print(over_18(15))

#7. A function that accepts a string and prints the string in reverse (no return value).
def reverse_str(str):
    print(str[::-1]) 
reverse_str("Hello World")