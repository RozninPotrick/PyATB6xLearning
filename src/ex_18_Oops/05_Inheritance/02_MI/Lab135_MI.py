class Father1:

    def money(self):
        print("F1 Money")

class Father2:

    def money(self):
        print("F2 Money")

class Child(Father1, Father2): # MRO (Method Resolution Order) parent class method is called first. eg Whose money --> F1 Money
#class Child(Father2, Father1) # output -> F2 Money
        def give_money(self):
          print("Child Money")
          self.money()

c = Child()
c.give_money()

