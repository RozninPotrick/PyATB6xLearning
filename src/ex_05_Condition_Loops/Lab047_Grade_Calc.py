# Grade Calculatior:
# Write a program that calculates and displays the letter grade
# for a given numerical score (eg. A, B, C, D, or F)
# based on the following grading scale

# A: 90-100
# B: 80-89
# C: 70-79
# D: 60-69
# F: 0-59

# Logic Building formula
# 1 -> User Input - score -> int
# 2 -> o/p - str -> A, B

score = int(input("enter a score: ").strip())

if score > 100 or score <= 0:
    print("You are a Superman!!, you can't get a grade!!")
else:
    if score >= 90 and score <= 100:
        print("Your grade is A")
    elif score >= 80 and score < 90: # or write <= 89
        print("Your grade is B")
    elif score >= 70 and score < 80: # or write <= 79
        print("Your grade is C")
    elif score >= 60 and score < 70: # or write <= 69
        print("Your grade is D")
    else:
        print("Your grade is F")

