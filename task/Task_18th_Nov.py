# Build a Test Framework with Encapsulation + Inheritance
#🎯 Goal:
# Create a simple automation structure that uses:
#A BaseTest class for setup/teardown (Parent class)
#A LoginTest class that inherits BaseTest (Child class)
#Encapsulate sensitive data (like credentials) as private variables

#✅ Requirements:

# Create a BaseTest class:
# Has a protected variable _driver = "Chrome".
# Method setup() prints "Launching browser: Chrome".
# Method teardown() prints "Closing browser".
# Create a LoginTest class that inherits BaseTest:
# Has private variables for username and password.
# Method run_test() that prints:
# "Running login test with user: <username>".
# Use encapsulation: access private vars only through a method (e.g., get_user()).
# Create an object of LoginTest and call:
# setup()
# run_test()
# teardown()

from dotenv import load_dotenv
import os

from task.Task007 import username


class BaseTest:

    _driver = "Chrome"

    def setup(self):
        _driver = "Chrome"
        print(f"Launching browser:",self._driver)

    def teardown(self):
        print("Closing browser")

class LoginTest(BaseTest):

    def __init__(self, usernameGiven, passwordGiven,):

        self.__username = usernameGiven
        self.__password = passwordGiven

    def run_test(self):
        load_dotenv()


        if self.__username == os.getenv("USERNAME"):
            print(f"Running login test with username:" ,self.__username)
        else:
            pass


username1 = input("Enter username: ")
password = input("Enter password: ")


ref_object = LoginTest(username, password)
ref_object.setup()
ref_object.run_test()
ref_object.teardown()



