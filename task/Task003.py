# write a Python program to calculate the
# area of a circle given its radius the formula
# ```area=  πxr^2```(Take pie as 3.14)
import math


# i/p - r - float
# o/p - string formatted output of area.

# Logic Building Formula
# || Step 1 ||
# Figure out input and output
# input -> r -> data type -> float
# pi = 3.14
# power -> pow or ** -> any
# o/p -> String -> float - area, print area

# || step 2 ||
# rough logic = area = 3.14 * pow(r,2)

# || step 3 ||
radius = float(input("Enter the radius of the circle\n"))
print(radius)

# By importing math you dont need to write pie value
#area = 3.14 * (radius ** 2)
area = math.pi * (radius ** 2)
#area = 3.14 * (pow(radius, 2))
print("Area of the circle is -> ", area)

# String data formatting, Pyhon f_strings, formatted string literals(only use in Flaot and .2f will give only last two digit decimal number.
print(f"The area of the circle is  -> {area:.2f}")

#r = 2.2
#result = 3.14 * r ** 2
#print(result)
