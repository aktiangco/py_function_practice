# arb_args - Takes in any number of arguments and prints them one at a time.
def arb_args(*args):
    for any in args:
        print(any)
arb_args("Allan", 35, "loco moco")       
        
# inner_func - Takes in two integers. Two nested functions should perform separate, distinct math operations using the integers. The result of both nested functions should then be added together and printed.
def inner_func(x,y):
    def inner_1():
        return x + y
    def inner_2():
        return x - y
    print(inner_1() + inner_2())

inner_func(10, 5)

# lunch_lady - Takes in two strings: a student's name and their lunch preference. The function should print both strings. If a lunch preference is not given, "Mystery Meat" should be printed instead.
def lunch_lady(student_name, preference=None):
    if preference is None:
        preference = "Mystery Meat"
        
    print(f"{student_name} wants {preference} for lunch.")

lunch_lady("Allan", "loco moco")
lunch_lady("Marlon")

# sum_n_product - Accepts two integers and returns both the sum and the product.
def sum_n_product(num1, num2):
    return num1 + num2, num1 * num2

result = sum_n_product(11,31)
print(result)

# alias_arb_args - Should be arb_args but assigned an alias. Remember, variables can hold functions in Python just like they can in JS. Alternatively, you can call a function from inside another function.
def arb_args(*foods):
    for food in foods:
        print(food)

food_foods = arb_args

food_foods("apples", "banana","strawberry")


# arb_mean - Accepts any number of integers and prints their average.
#*  def arb_mean(*args):
#*     total = 30
#*     for a in args:
#*         #a = 1
#*         total =+ a
#*     print(30/6)

#* arb_mean(20, 25, 26, 28)

# TODO work on this

# arb_longest_string - Accepts any number of strings and returns the longest one.
def arb_longest_string(*args):
    longest = ""
    for arg in args:
        if len(arg) > len(longest):
            longest = arg
    return longest

result = arb_longest_string("watermellon", "banana", "apple")
print(result)
