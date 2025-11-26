class Person:
    # attributes

    name = None
    id = None
    age = None
    email = None
    height = None
    gender = None
    phone = None
    address = None

    # Behaviour

    def talk(self): # self - this self will be first argument
        print("I can talk")

    def walk(self):
        print("I can walk")

    def method_walk_return(self):
        return "I am walking"

    def sleep(self, name): # Arg with no return
        print("I am a Method")
        print("sleep", name)

    def sleep2(self, name): # Arg with Return
        print("I am a Method")
        return None

def function_outside():
    print("Outside")

# Create an object of the class
# ObjectRef = ClassName() -> object

geeta = Person()
geeta.talk()
amit = Person()
amit.walk()
navita = Person()
navita.sleep("Pramod")
print(geeta.method_walk_return())
print(geeta.name)

#navita.method_walk_return()



