# Problem Find the Max between 3 numbers

# logic Building

# User inputs i/p - num1, num2, num3 -> int
# o/p -> int or String with max number.

num1 = int(input("Enter a number\n"))
num2 = int(input("Enter another number\n"))
num3 = int(input("Enter a third number\n"))

if num1 >= num2 and num1 >= num3:
    print("Maximum", num1)
elif num2 >= num3 and num2 >= num1:
    print("Maximum", num2)
else:
    print("Maximum", num3)

