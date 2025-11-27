class Bank:

    def __init__(self, account_number, balance):
        self.__account_number = account_number # private
        self.__balance = balance # private

    def check_balance(self):
        print(self.__balance)

    def deposit(self, amount):
        self.__balance = self.__balance + amount

    def show_me_account_number(self,is_auth):
        if is_auth == True:
            print(self.__account_number)
        else:
            print("Not Allowed")

icici = Bank(9878456123,100)
icici.check_balance()

icici.deposit(100000000)
icici.check_balance()

# print(icici.__account_number)
# if you are cashier you can see the a?c because of the encapsulation
icici.show_me_account_number(True)
