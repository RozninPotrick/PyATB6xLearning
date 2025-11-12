import  math

# def give-me_power(num)
#   return math.pow(num, 2) # Try to slove like this
# op = give_me_power(10)
# print(op)

op = lambda num : math.pow(num,2)
result = op(3)
print(result)

# or
# print(op(3)

# or
op1= lambda : math.pow(int(input("Enter a number")) , 2) # not to be used
print(op1())