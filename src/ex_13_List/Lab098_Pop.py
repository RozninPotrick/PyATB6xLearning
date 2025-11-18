squares = [1,4,9,16,25]
print(squares)

# pop() - remove the last element and return the element also
#squares.pop() - cannot do like this because it will give only remove value
#print(squares)

print(squares.pop()) # will remove and gives you return values
print(squares)
print(squares.pop(1)) # will remove the particular element not last element
print(squares)

# clear() - delete the list
squares.clear()
print(squares)

# index(element, start, end)
# Returns the index of the first occurrence of the element
numbers = [10,20,30,40,20,50]
print(numbers.index(30))

# count() - count the particular numbers occurance
print(numbers.count(20))
print(numbers.count(30))

numbers.sort()
print(numbers)

numbers.sort(reverse=True)
print(numbers)

numbers.reverse()
print(numbers)

numbers.reverse()
print(numbers)

print(max(numbers))
print(min(numbers))
print(sum(numbers))

# slicing
print(numbers)
print(numbers[1:4]) # from index 1 to 3
print(numbers[-1])

# In function -> checking what is present in a list
print("apple" in numbers)
print(20 in numbers)

# List Creation and comprehension
# range(1,5) -> list
l = list(range(1,5))
print(l)

# Nested list -> add list of list
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(matrix)
print(matrix[1][2])

# del statement - deletes an element by index or the whole list.
del numbers[1]
print(numbers)





