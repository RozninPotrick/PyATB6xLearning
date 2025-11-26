class Dog:

    name = None
    breed = None
    height = None
    weight = None
    race = None

    def __init__(self, nameGiven, breedGiven):
        print("para Constructor")
        self.name = nameGiven
        self.breed = breedGiven

    def bark(self):
        print("Barking")

    def sleep(self):
        print("Who is sleeping -> " + self.name)

    def talk(self):
        pass

#chow = Dog()
#chow.bark()
#chow.sleep()
#chow.talk()

chow = Dog("Love","Mastiff")
rancho = Dog("Tyzer", "desi")

chow.sleep()


