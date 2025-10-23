# write a program to take a user age and
# let him know if he can go the club
# 21

# Logic Building Formula

# Step 1
# i/p - age, int
# o/p - String (result -> can go to club or not

# step 2. Rough logic ( brute force)
"""
age > 21 -> print can go
age < 21 -> print can't go

"""

# Step 3. Write the logic

age = int(input("Enter a age\n"))

if age >= 21:
    print("yes, you can go to club")
else:
    print("no, you can't go to club")

# step 4. Check for the edge cases.
# We should consider edge cases such as:
# Negative ages or extremely high values -> program will break.
# Non-numeric input - ABC
# Age which is valid. > 130

# Step 5. Optimize the code.
# handle all the edges.

