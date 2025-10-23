# Problem to find the max between two.

# Logic Building Formula

# 1. user inputs i/p -> two integers
# 2. o/p -> int 1 which is greater max number it will return
# 31.4 or 45.34 - float

num1 = float(input("Enter a number: "))
num2 = float(input("Enter another number: "))

if num1 >= num2:
    print("Maximum" , num1)
else:
    print("Maximum", num2)

# if you want positive number
# if num1 > 0 and num2 > 0:
#   print("Number should be positive")

num3 = float(input("Enter a number: "))
num4 = float(input("Enter another number: "))
if num3 > 0 and num4 > 0:
    print("Number should be positive")
else:
    print("enter a valid number")

