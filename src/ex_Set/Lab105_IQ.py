# Find the first non-repeating character in a string using sets
# swiss -> s-x, w - answer

print("swiss".count("s"))
print("swiss".count("w"))

def first_non_repeating(string):
    for char in string:
        if string.count(char) == 1:
            return char
    return None

print(first_non_repeating("swiss"))
print(first_non_repeating("annusinha"))

string = "swiss"
for i in string:
    print(i)

