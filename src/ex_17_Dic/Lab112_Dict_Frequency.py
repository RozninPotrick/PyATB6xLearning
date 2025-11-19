dict1 = {"a": 1, "b": 2, "c": 3}
print(dict1)
print(dict1.keys())
print(dict1.values())
print(dict1.items())

dict2 = {"a": 1, "b": 2}

# To find the missing iteams
missing_keys = set(dict1.keys()) - (dict2.keys())
print(missing_keys)

