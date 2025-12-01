try:
    a = int(input("Enter num 1"))
    b = int(input("Enter num 2"))
    c = a/b
    print(c)
except ValueError:
    print("Value error")
except ZeroDivisionError:
    print("Zero Division Error")
else: # Runs only if try block suceeds
    print(c)
finally:
    print("I will always execute")