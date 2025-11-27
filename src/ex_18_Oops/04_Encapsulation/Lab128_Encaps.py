class VWOLoginPage:

    def __init__(self,email_arg, password_arg):
        self.email = email_arg
        self.password = password_arg

    def login_confirmation(self):
        if self.email == "Rose@gmail.com" and self.password == "123456" :
            print("Login Successful")
        else:
            print("Login Failed")

email = input("Enter the vwo login email")
password = input("Enter the vwo login password")

vwo_ref = VWOLoginPage(email, password)
vwo_ref.login_confirmation()