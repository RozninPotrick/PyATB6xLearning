# *
# **
# ***
# ****
# *****

# simple
for i in range(1,6):
    print("*" * i)

# Actual way
rows = int(input("Enter the rows for the right angle triangle"))

for i in range(1, rows+1):
    for j in range(i):
        print("*", end="")
    print()