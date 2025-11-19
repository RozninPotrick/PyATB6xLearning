test_result = ["PASS","FAIL","PASS","SKIP","FAIL"]

pass_give = list(filter(lambda x: x == "PASS", test_result))
print(pass_give)

# 2nd Example

list_student = [50,51,100]

def keep(x):
    if x > 50:
        return True

all_student = list(filter(keep, list_student))
print(all_student)

