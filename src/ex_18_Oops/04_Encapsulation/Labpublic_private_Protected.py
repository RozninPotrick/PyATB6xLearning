class TestExample:

    def __init__(self):
        self.driver = "chrome"
        self._config = "STAG"
        self.__api__key = "ABC12345"

    def show(self):
        print(f"Driver: {self.driver}")
        print(f"Config: {self._config}")
        print(f"API Key : {self.__api__key}")

    def __private_method1(self):
        pass

    def __private_method2(self):
        pass

    def work(self):
        self.__private_method1()
        self.__private_method2()

obj_ref = TestExample()
obj_ref.show()

# access levels:
print(obj_ref.driver)      # public - accesible
print(obj_ref._config)     # protedted - accessible but not recommemded
#print(obj_ref.__api__Key) # private - attribute Error , not allowed

obj_ref.work()