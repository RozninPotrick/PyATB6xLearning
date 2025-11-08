# User defined
# 1. They can't return -> non return
# 2. They can return something
# 3. They have parameters
# 4. They don't have parameters / arguments

import math

# built in function
result = max(5,3)
print(result)

name = "Roznin"
print(name)

# 1. They can't return -> no return
# No Return type and No Parameter / argument - NRNP

def greet():
    print("Hello")

greet()

# 2. No Return Type and with Argument / Parameters

def greet_by_name(name):
    print("Hello ," , name)

greet_by_name("Roznin")

def tell_yor_age(age):
    print("I'm " , age)

tell_yor_age(35)

# 3. no Return Type and with default argument( postional arguments0

def say_hello_default_arg(name = "Roznin"):
    print("Hello ," , name.upper())

say_hello_default_arg()
say_hello_default_arg("Potrick")

def tell_me_your_age(age = 35):
    print("I'm " , age)

tell_me_your_age()
tell_yor_age(36)

# multiple arguments / parameters

def multiple_args(name1 = "A", name2 = "B"):
    print("mul ->", name1, name2)

multiple_args(name1 = "A", name2 = "B")
multiple_args()
multiple_args(name1 = "Rose")
multiple_args(name2 = "Love")
multiple_args(name2 = "Rose", name1 = "Love" )

# Multiply parameters and  it returns

#1
def sum_of_two(a, b):
    return a + b

result = sum_of_two(1, 2)
print(result)

# 2
def sum_of_two_Numbers_with_default(num1=100,num2 =200):
    print("I will add the two numbers")
    return num1 + num2

result = sum_of_two_Numbers_with_default()
print(result)
result = sum_of_two_Numbers_with_default(num1=11, num2=20)
print(result)

# 3.
def sub_of_two_numbers_with(c,d):
    print("I will subtract the two numbers")
    return c - d

result = sub_of_two_numbers_with(1, 2)
print(result)








