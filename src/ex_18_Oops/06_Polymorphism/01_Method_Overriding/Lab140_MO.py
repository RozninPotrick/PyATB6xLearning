class BaseTest:

    def run(self):
        print("Running generic test")

class LoginTest(BaseTest):

    def run(self):
        print("Running login test")

#t = LoginTest() whoever object is created will execute
t = BaseTest()
t.run()