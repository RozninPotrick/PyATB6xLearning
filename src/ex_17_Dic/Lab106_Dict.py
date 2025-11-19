my_dict = {
    "name": "Amanda",
    "age": 22,
    "role" : "SDET",
    "exp": 3

}

print(my_dict)
print(my_dict["name"])
print(my_dict["age"])

my_dict["age"] = 32
print(my_dict)

del my_dict["age"]
print(my_dict)

# for loop
for key,values in my_dict.items():
    print(key, values)
    print(key)
    print(values)

print("age" in my_dict)
print("role" in my_dict)
