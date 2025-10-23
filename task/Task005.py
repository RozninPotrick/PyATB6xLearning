# Q1 You receive an API response code from your test script.
# Write an if-else block to check whether the response is successful (status code 200) or not.
# I/P response = 404 , O/P ❌ Failed API Request
# I/P response = 200 , O/P ✅ Passed API Request

status_code = int(input("Enter a status code:".strip()))
if status_code == 200:
    print("Passed API request")
else:
    print("Failed API request")

# Q2In automation, you often compare expected and actual outputs.
# Write code to check if a test case passed or failed.
# expected_title = "Dashbpord"
# actual_title = "Dashboard "
# ✅ Test Passed – Title matches

expected_title = "Dashbpord"
actual_title = "Dashoard"
if expected_title.strip()  ==  actual_title.strip():
    print("Test passed-Title matches")
else:
    print("Test failed-Title matches")

