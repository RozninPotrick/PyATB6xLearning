class Home:

    def __init__(self):
        self.public_var = "Father"
        self._protected_var = "Brother"
        self.__private_var = "Baby"

    def mom(self):
        print(self.public_var)
        print(self.__private_var)
        self.__wife()

    def __wife(self):
        print("private wife")



obj_ref = Home()
print(obj_ref.public_var)

# obj_ref.__wife
# obj_ref.__private_var

obj_ref.mom()

print(obj_ref._protected_var) # Technically accessible but not recommended
