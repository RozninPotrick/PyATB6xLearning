a = int(input("Enter num 1"))
b = int(input("Enter num 2"))
try:
    c = a/b
    print(c)
except ZeroDivisionError:
    print("Error because of the Zero Div b != 0")
