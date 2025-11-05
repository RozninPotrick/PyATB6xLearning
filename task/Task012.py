#Q - Create a function which will take a positive number from the user and perform square of the number?
#i/o = 3
#o/p = 9

def positive_number(num):
    return num ** 2

square = positive_number(int(input("Enter a number: ")))
print("Square of positive number:" , square )



#Q - Create a function which will take the 3 values from the user, which are length of the triangle.  side1, side2, side2
#i/p - int side1 == side2 =side3 → isoceles
#o/p = result in string - iso, eq, scalene

def value_of_triangle(num1, num2, num3):
    if num1 == num2 == num3:
        print("It is a equilateral triangle")
    elif num1 == num2 or num2 == num3 or num3 == num1:
        print("It is a isosceles triangle")
    else:
        print("It is a scalene triangle")

value_of_triangle(8,6,9)
value_of_triangle(num1=5,num2=5,num3=5)

side1 = int(input("Enter the side 1 :"))
side2 = int(input("Enter the side 2 :"))
side3 = int(input("Enter the side 3 :"))
value_of_triangle(side1,side2,side3)
