
# *! To check: python3 day1/python_practice.py

def hello():
    print("Hello Master!")

def pack(x, y, z):
    my_list = [x, y, z]
    return my_list

def eat_lunch(lunch):
    if len(lunch) == 0: #len() Return the length (the number of items) of an object
        print("My lunchbox is empty!")
    else:
        print("First I eat", lunch[0])
        for item in lunch[1:]:
            print("Next I eat", item)
            
hello()
print(pack(5, 31, 87))
eat_lunch([])
eat_lunch(["musubi", "loco moco"])

