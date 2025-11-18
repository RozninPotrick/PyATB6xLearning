cities = ("London", "Paris", "Los Angeles", "Tokyo")
print(cities)
print(len(cities))
print(cities[0])
print(cities[-1])
print("Paris" in cities)
print("Mumbai" in cities)

t = (1,2,3,True,23.22)
print(t)

t1 = ()
print(t1)

ENV_API_URLS = tuple(["abc.com/get","xyz.com/get","qwe.com/get"])
print(ENV_API_URLS)

# for loop to do tuple
colors = ("red", "green", "blue")
for c in colors:
    print(c)

numbers = "pramod" * 3
print(numbers)

numbers = (1,2) * 3
print(numbers)

print( "-----------")

nums = (1,2,2,3,2)
print(nums)
print(len(nums))
print(nums.count(2))
print(nums.index(3))
print(nums)

my_list = [1,2,3]
print(my_list)

#convert into list
my_tuple = list(my_list)
print(my_tuple)

# convert into tuple
back_to_tuple = tuple(my_list)
print(back_to_tuple)
print(max(back_to_tuple))

print(nums[0:2])

















