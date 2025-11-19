nums = [1,2,3,4,5,6]

def evn_num(x):
    return x % 2 == 0

even_numbers = list(filter(evn_num, nums))
print(even_numbers)