# function that returns the maximum value from a dictionary
# {"a" : 10, "b" : 20, "c" : 30}

def max_value_dict(dictionary):
    return max(dictionary.values())

print(max_value_dict({"a": 10, "b": 20, "c": 30}))

def min_value_dict(dictionary):
    return min(dictionary.values())

print(min_value_dict({"a": 10, "b": 20, "c": 30}))

def min_value_keys_dict(dictionary):
    return  min(dictionary.keys())
print(min_value_keys_dict({"a": 10, "b": 20, "c": 30}))



