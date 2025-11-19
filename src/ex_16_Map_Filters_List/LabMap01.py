numbers = [1,2,3,4,5]

def sq(x):
    return x ** 2

sq_all_numbers = list(map(sq, numbers))
print(sq_all_numbers)

# for loop for suare
for i in numbers:
    sq_all = sq(i)
    print(sq_all)


def add(x):
    return sum(numbers)

add_numbers = list(map(add, numbers))
print(add_numbers)


#for i in numbers:
#    add_all = sum(numbers)
#    print(add_all)