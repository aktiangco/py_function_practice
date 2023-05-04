# Activity: Practice with Functional Programming
# *! To check: python3 day3/functional_programming.py
'''
Problem 1: Write a function flatten_dict to flatten a nested dictionary by joining the keys with . character.

>>> flatten_dict({'a': 1, 'b': {'x': 2, 'y': 3}, 'c': 4})
output: {'a': 1, 'b.x': 2, 'b.y': 3, 'c': 4}
'''
def flatten_dict(d):
    # create an empty dictionary to store the flattened dictionary
    result = {}
    
    # iterate over the key-value pairs in the input dictionary
    for key, value in d.items():
        # if the value is itself a dictionary, recursively call flatten_dict on it
        if isinstance(value, dict):
            subdict = flatten_dict(value)
            # for each key-value pair in the flattened sub-dictionary, add it to the result
            for subkey, subvalue in subdict.items():
                result[key + '.' + subkey] = subvalue
        # if the value is not a dictionary, simply add the key-value pair to the result
        else:
            result[key] = value
    
    # return the flattened dictionary
    return result

print(flatten_dict({'a': 1, 'b': {'x': 2, 'y': 3}, 'c': 4}))
    


'''
Problem 2: Write a function unflatten_dict to do reverse of flatten_dict.

>>> unflatten_dict({'a': 1, 'b.x': 2, 'b.y': 3, 'c': 4})
output: {'a': 1, 'b': {'x': 2, 'y': 3}, 'c': 4}
'''
def unflatten_dict(d):
    result = {}
    for key, value in d.items():
        # Split the key into its parts using the . character as a delimiter
        parts = key.split('.')
        subdict = result
        # For each part of the key, either add it to the subdict if it doesn't exist
        # or descend into the subdict to continue building the hierarchy
        for part in parts[:-1]:
            if part not in subdict:
                subdict[part] = {}
            subdict = subdict[part]
        # Finally, add the value to the appropriate place in the hierarchy
        subdict[parts[-1]] = value
    return result

print(unflatten_dict({'a': 1, 'b.x': 2, 'b.y': 3, 'c': 4}))


'''
Problem 3: Write a function treemap to map a function over nested list.

>>> treemap(lambda x: x*x, [1, 2, [3, 4, [5]]])
output: [1, 4, [9, 16, [25]]]
'''

def treemap(func, lst):
    """
    Applies a function to each element of a nested list.
    """
    result = []
    for item in lst:
        if isinstance(item, list):
            result.append(treemap(func, item))
        else:
            result.append(func(item))
    return result

print(treemap(lambda x: x*x, [1, 2, [3, 4, [5]]]))