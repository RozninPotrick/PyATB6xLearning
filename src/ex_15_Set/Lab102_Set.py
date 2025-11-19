# SET
# Collection of unique elements
# {} - parenthesis

list_of_unique_items = {1,2,3,4,4,5,5}
print(list_of_unique_items)

List1 = [45.2,33,33,45,21]
#set1 = set(List1) # or you can write like this to convert into set
print(set(List1))

t = ("TheTestingAcademy", "for", "TheTestingAcademy")
print(t)
print(set(t))

# mixed elements
mixed = {1, "QA", True, 3.5} # 1 = true in python thats why it wont print True in this case
print(mixed)
mixed = {2,"QA", True}
print(mixed)

# for loop
for item in mixed:
    print(item)

#add elements
mixed.add(4)
print(mixed)
mixed.remove(4)
print(mixed)

empty = set()
print(empty)
print(len(empty))
print(type(empty))







