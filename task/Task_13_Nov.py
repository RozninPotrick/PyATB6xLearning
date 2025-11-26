# create a Person class where we will have five attributes and five behaviors.
# Make sure that each type of function is used, and I want you to also create the print function,
# which will print all the instance variable values.

class Person:

    name = None
    age = None
    weight = None
    height = None
    occupation = None

    def __init__(self, nameGiven, ageGiven, weightGiven, heightGiven, occupationGiven):
        self.name = nameGiven
        self.age = ageGiven
        self.weight = weightGiven
        self.height = heightGiven
        self.occupation = occupationGiven

    def name_of_person(self):
        print("I am Rose")

    def walk(self):
        print("I am walking")

    def talk(self):
        print("Talking")

    def height_value(self):
        print("5.5")

    def occupation_of_person(self):
        print("QA")


    def display_details(self):
        print("Name is ",self.name, "Age is ",self.age, "Weight",self.weight, "Height",self.height)



obj_ref = Person("Rose",40,66,5.5,"QA")
obj_ref.name_of_person()
obj_ref.walk()
obj_ref.talk()
obj_ref.height_value()
obj_ref.occupation_of_person()
print(obj_ref.name)
obj_ref.display_details()





#You need to create a calculator function,
# but the calculator function has to take the value from the parameterized constructor.
# So while creating the object, you will pass the parameters and
# that will basically return the sum of the two numbers, multiplication of two numbers.

class Calc:
    a = None
    b = None

    def __init__(self, aGiven, bGiven):
       self.a = aGiven
       self.b = bGiven

    def sum(self):
        return self.a + self.b

    def mul(self):
        return self.a * self.b

obj_ref = Calc(5, 6)
print(obj_ref.sum())
print(obj_ref.mul())