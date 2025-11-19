squares = {x ** 2 for x in range(5)} # should not to be use in set as a oneliner code
print(squares)

# Frozen set(Immutable set)
# A frozenset cannot be changed after creation or add etc

my_list = [1, 2, 3,4]
fset = frozenset(my_list)
print(fset)

# eg.
#fset.add(10)
#print(fset)
