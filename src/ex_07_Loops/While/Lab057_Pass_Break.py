for i in range(0, 10, 1):
    if i == 6 or i == 5:
        print(i)
    else:
        pass # do nothing

# Exp and Result table (ERT)
# | i | Condition       |  O/p
# | 0 | 0 == 6 -> False |  o/p  = Nothing will be printed
# | 1 | 0 == 6 -> False |  o/p  = Nothing will be printed
# | 2 | 0 == 6 -> False |  o/p  = Nothing will be printed
# | 3 | 0 == 6 -> False |  o/p  = Nothing will be printed
# | 4 | 0 == 6 -> False |  o/p  = Nothing will be printed
# | 5 | 0 == 5 -> True  |  o/p  = 5
# | 6 | 0 == 5 -> True  |  o/p  = 6
# | 7 | 0 == 6 -> False |  o/p  = Nothing will be printed
# | 8 | 0 == 6 -> False |  o/p  = Nothing will be printed
# | 9 | 0 == 6 -> False |  o/p  = Nothing will be printed
# | 10| 0 == 6 -> False |  o/p  = exit -> for loop finished