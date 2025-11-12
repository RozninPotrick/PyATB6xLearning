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
print(numbers[1:4])
print(numbers[-1])






