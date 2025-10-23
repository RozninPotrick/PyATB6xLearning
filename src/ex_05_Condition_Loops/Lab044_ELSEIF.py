# Find the number is even or odd

num = int(input("Enter a number: ").strip())

if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# Find the positive number is even or odd

num1 = int(input("Enter a number: ").strip())

if num1 >=0 :
    if num1 % 2 == 0:
        print("Even")
    else:
        print("Odd")
else:
    print("Negative number")

# You can write short one liner coditions using ternary operator:
if num1 >= 0:
    print("Even" if num1 % 2 == 0 else "Odd")
else:
    print("Negative number")


