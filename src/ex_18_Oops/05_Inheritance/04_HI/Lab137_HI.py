class BaseTest():

    def setup(self):
        print("setup from BaseTest")

class LoginTest(BaseTest):

    def run(self):
        print("Running Login Test")

class SignupTest(BaseTest):

    def stop(self):
        print("Running Signup Test")


LoginTest().run()
LoginTest().setup()
SignupTest().stop()
SignupTest().setup()
