my_list = [1,2,3]
print(my_list)
my_list[0] = "Rozy"
my_list[1] = "Love"
print(my_list)

for iteam in my_list:
    print(iteam)

# range() this also return the list

for i in range(1, 5):
    print(i)

# Indexing
my_list = [1,2,3]
print("element at the index 0 -" , my_list[0])
print("element at the index 1 -" , my_list[1])
print("element at the index 2 -" , my_list[2])

# append() - append/ add object to the end of the list
my_list.append(4)
print(my_list)

my_list.append(5)
print(my_list)

my_list.extend([7,8,9,10])
print(my_list)

my_list.insert(1, "Rose")
print(my_list)

my_list[5] = "Love"
print(my_list)

my_list.remove(8)
print(my_list)

my_copy_list = my_list.copy()
print(my_list)
print(my_copy_list)

my_copy_list.remove(3)
print(my_list)
print(my_copy_list)




