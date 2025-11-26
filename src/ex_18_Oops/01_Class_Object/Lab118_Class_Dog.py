class Dog:
    # attribute
    name = None
    breed = None
    height = None
    weight = None

    # Behaviour
    def bark(self):
        print("Barking")
        print(self.name)
        print(self.breed)

    def walk(self):
        print("Walking")

print("Outside")

chow = Dog()
chow.bark()
print((chow.name))

rancho = Dog()
rancho.walk()
print((rancho.weight))
