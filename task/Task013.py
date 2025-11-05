#🧩 1️⃣  Write a Function to Check Test Case Status
# Problem:
# Write a function check_status(status_code) that returns:
# "PASS" if status_code = 200
# "FAIL" if status_code = 400 or 500
# "UNKNOWN" otherwise
# Example Input & Output:
# print(check_status(200))   # PASS
# print(check_status(500))   # FAIL
# print(check_status(302))   # UNKNOWN

def check_status(status):
    if status == 200:
        print("PASS")
    elif status == 400 or status == 500:
        print("FAIL")
    else:
        print("Unknown")

check_status(200)
check_status(400)
check_status(500)
check_status(status=200)
check_status(int(input("Enter the number :")))