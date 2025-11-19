name = ["pramod", "dutta", "qa","lucky"]
print(name)

def upper_case(string):
    return string.upper()

s = upper_case("dutta")
print(s)

# To make name all in  uppercase from the list
upper_names = list(map(upper_case, name))
print(upper_names)