# Q1.Given a Number you need to calculate the factorial of that number
# n = 5
# Fact = 5×4×3*2*1 = 120
# Fact = 0 → 1,

num = int(input("Enter a number: "))
fact = 1 # Bydefault factorial is 1

if num < 0:
    print("Fact is not defined!")

if num  == 0 :
    print("Fact = ", fact)
else:
    for i in range(1, num+1): # num +1 is used to get numner 5
      fact = fact * i

    print("Factorial of : ", fact)









