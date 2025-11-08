#Q - Create a function which will take the 3 values from the user, which are length of the triangle.  side1, side2, side2
#i/p - int side1 == side2 =side3 → isoceles
#o/p = result in string - iso, eq, scalene

side1 = float(input("Enter the first side: "))
side2 = float(input("Enter the second side: "))
side3 = float(input("Enter the third side:"))

def classify_triangle(a,b,c):
    if a > 0 and b > 0 and c > 0:
        if a + b > c and a + c > b and b + c > a:
          if a == b == c :
             return "Equilateral"
          elif a == b or b == c or c == a:
             return "Isosceles"
          else:
             print("scalene")
    else:
        print("Not a valid length")

result = classify_triangle(side1,side2,side3)
#print(result)
print(f"The triangle is classified as: {result}")