# Just an example for global variable

a = 10 # variable everywhere in the program

class Person:
    b = 11  # Instance variable

    def print_info(self):
        c = 20 # Local varaible
        print(c)
        print(self.b)
        print(a)



object_ref = Person()
object_ref.print_info()
# not allowed
#print(a)
#print(b)
#print(c)