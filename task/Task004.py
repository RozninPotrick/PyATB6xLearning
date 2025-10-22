b = float(input("enter a base:"))
h = float(input("enter a height:"))
area = 1/2 * b * h
print("Area of the triangle: ", area)

number = float(input("enter a number:"))
if number > 100:
    print("number is greater than 100")
else:
    print("number is less than 100")

print("number is greater than 100" if number > 100 else "number is less than 100")