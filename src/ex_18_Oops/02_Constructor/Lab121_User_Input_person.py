class Person:
    name = None
    age = None
    phone = None
    occupation = None

    def __init__(self):
        self.name = input("What is your name\n")
        self.age = input("What is your age\n")
        self.phone = input("What is your phone\n")
        self.occupation = input("What is your occupation\n")

    def display_value(self):
        print("Name is " , self.name, "Age is " , self.age, "Phone is " , self.phone, "Occupation is " , self.occupation)

Rose_ref = Person()
Rose_ref.display_value()