class Dog:

    name = None
    age = None
    breed = None
    height = None
    weight = None

    def __init__(self):
        print("I will be called")

    def bark(self):
        print("I am barking")

    def sleep(self):
        print("I am sleeping")

    def talk(self):
        pass

chow_ref = Dog()
mow_ref = Dog()

print((chow_ref.name))
print((mow_ref.name))

Dog().bark()

