# Q1.Given a Number a number you need to calculate the factorial of that number
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





#Q2: An API sometimes fails due to network delays.
# Write a program to retry the API call 3 times until the response code becomes 200.
# If it still fails after 3 tries, print a failure message.
# Hint: Use a while loop with a counter.
# Hint: Use a while loop with a counter.
# Expected Output Example:
# Attempt 1: Response 500
# Attempt 2: Response 200
# ✅ Test Passed




# Q3 : Simulate a page loading check using a while loop.
# If page_loaded becomes True within 5 seconds, print success; else timeout.
# Hint: Use a counter (like wait_time) and break condition.

for i in range(6):
   if  i == 5:
      print("page_loaded")
   else:
       print("timeout")
