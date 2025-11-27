class Car:

    def __init__(self):
        self.public_pramod = "pramod"
        self.__private_baby = "pass123"

    def nanny(self):
            self.__password_yogesh_private = "123"

obj_ref = Car()
obj_ref.nanny()
print(obj_ref.public_pramod)
#print(obj_ref.__private_baby) # not possible because its private


