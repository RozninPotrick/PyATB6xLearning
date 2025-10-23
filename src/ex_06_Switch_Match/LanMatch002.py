print("Enter the which Test you want to run")
test_type = input("Enter the test type: API, UI, Performance, Security")

match test_type:
   case "API":
     print("we are running a Postman API Testcase.")
   case "UI":
       print("we are running a Selenium UI Testcase.")
   case "Performance":
       print("we are running a Performance Testcase.")
   case "Security":
       print("we are running a Security Testcase.")
   case _:
       print("Invalid Type")
