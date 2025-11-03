for i in range(0,10): # Interview Question
    if i == 5:
        print("Five")
    else:
        print(i)

# Exp and Result table (ERT)
# | i | Condition       |  O/p
# | 0 | 0 == 5 -> False |  o/p  = 0
# | 1 | 0 == 5 -> False |  o/p  = 1
# | 2 | 0 == 5 -> False |  o/p  = 2
# | 3 | 0 == 5 -> False |  o/p  = 3
# | 4 | 0 == 5 -> False |  o/p  = 4
# | 5 | 0 == 5 -> True  |  o/p  = FIVE
# | 6 | 0 == 5 -> False |  o/p  = 6
# | 7 | 0 == 5 -> False |  o/p  = 7
# | 8 | 0 == 5 -> False |  o/p  = 8
# | 9 | 0 == 5 -> False |  o/p  = 9
# | 10| 0 == 5 -> False |  o/p  = exit -> for loop finished