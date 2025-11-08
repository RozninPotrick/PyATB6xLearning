# Create a program to sum of three number from the user input
# if user doesn't enter any number' , use default as 100,200,300

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

def sum_of_three_numbers(num1=100,num2 =200,num3 =300):
    print("I will add the three numbers")
    return num1 + num2 + num3 + num1

result = sum_of_three_numbers(num1,num2,num3)
print(result)
result = sum_of_three_numbers()
result1 = sum_of_three_numbers(num2 = 10)
print(result)
print(result1)