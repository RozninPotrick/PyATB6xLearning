a = {1,2,3}
b = {3,4,5}
print(a | b)
print(a.union(b))

print(a.intersection(b))
print(a & b)

print(a.difference(b))
print(a - b)
print(b - a)

print(a ^ b)

# more example
set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}

print(set1)
print(set2)

print(set1 | set2) # union
print(set1 & set2) # intersection
print(set1 - set2) # difference
print(set2 - set1)
print(set1 ^ set2) # symmetric

